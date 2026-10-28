"""Inspect the six supplied teaching fixtures; no rendering, network or uploads.

This is a bounded teaching example, not a general SVG sanitizer or validator.
Counts include definitions and hidden elements; they do not measure visible art.
"""
import collections, json, pathlib, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
SVG='{http://www.w3.org/2000/svg}'
SHAPES={'rect','circle','ellipse','line','polyline','polygon'}

def inspect(path):
    raw=path.read_bytes()
    if len(raw)>32768:raise ValueError('Teaching fixture exceeds 32 KiB limit')
    text=raw.decode('utf-8')
    if '<!DOCTYPE' in text.upper() or '<!ENTITY' in text.upper():
        raise ValueError('Declarations are outside this teaching fixture format')
    root=ET.fromstring(text)
    if root.tag!=SVG+'svg':raise ValueError('Expected SVG namespace root')
    tags=collections.Counter(e.tag.removeprefix(SVG) for e in root.iter() if e.tag.startswith(SVG))
    counts={k:tags[k] for k in ['path','image','text','use']}
    counts['basic_shape']=sum(tags[k] for k in SHAPES)
    refs=[]
    for e in root.iter():
        value=e.get('href') or e.get('{http://www.w3.org/1999/xlink}href')
        if value:
            kind='local fragment' if value.startswith('#') else 'data URI' if value.startswith('data:') else 'external or relative reference'
            refs.append({'element':e.tag.removeprefix(SVG),'kind':kind})
    return {'counts':counts,'references':refs,'bytes':len(raw)}

if __name__=='__main__':
    expected=json.loads((ROOT/'expected.json').read_text(encoding='utf-8'))
    results={name:inspect(ROOT/name) for name in expected}
    errors=[name for name in expected if results[name]['counts']!=expected[name]]
    report={'fixtures':results,'passed':len(expected)-len(errors),'total':len(expected),'errors':errors,'meaning':'Structural counts only; no safety, rendering, scale, geometry-quality or cutter-compatibility verdict.'}
    print(json.dumps(report,indent=2))
    raise SystemExit(bool(errors))
