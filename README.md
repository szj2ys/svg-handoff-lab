# SVG handoff lab

Six tiny, original synthetic files show why an SVG extension is not a complete description of the artwork. They require no account, web service or private image. The examples are small enough to read side by side with their XML.

Download or clone this repository, then run `python inspect_fixtures.py` with Python 3.9 or later in this directory. No packages need installing. The script reads only the named fixtures and prints structural counts. It makes no network requests and does not render files. Its counts include definitions; they are not counts of visible objects.

| File | Lesson | Expected observation |
|---|---|---|
| 01-path.svg | A filled path | One path, no image |
| 02-basic-shapes.svg | Vector geometry need not use paths | One rectangle and one circle |
| 03-embedded-raster.svg | SVG can contain raster data | One image with a PNG data URI |
| 04-mixed.svg | Files can mix formats | One image and one path |
| 05-live-text.svg | Text is distinct from outlines | One text element; rendering depends on fonts |
| 06-local-use.svg | A reference can reuse local geometry | A defined path and a use reference |

Open only these known synthetic fixtures in an editor if making tutorial screenshots. Compare the object tree with the XML. Do not tell readers to execute unknown SVG files as a security test. The script is a teaching example, not a hardened untrusted-file parser, sanitizer or visual validator.

Practical handoff checklist:

1. Establish whether the recipient needs editable artwork, a printed image or a cut path.
2. Inspect image references, geometry, text and reused elements separately.
3. Compare the outline, holes and fine details against the source at intended size.
4. Open the result in the intended application and check scale, grouping and operation assignments.
5. Keep the source and a copy of the unmodified trace so cleanup is reversible.

An image element may reference a raster format or SVG. The absence of images does not prove a file contains only paths, and the presence of paths does not prove accuracy. See the [SVG 2 embedded-content specification](https://www.w3.org/TR/SVG2/embedded.html#ImageElement) and [pic2svg's inspection guide](https://pic2svg.com/how-to-check-if-svg-is-a-real-vector/).

## Scope and reuse

This is a six-case teaching lab, not an automatic preflight checker. The related [SVG Structure Inspector](https://github.com/szj2ys/svg-structure-inspector) is a separate, more extensive inspection utility. This lab has no dependency on that project or on Pic2SVG.

The fixtures, bounded Python example and explanations were prepared with AI assistance for Pic2SVG's educational resources. They contain synthetic geometry and a tiny embedded raster, not customer artwork. You can adapt and redistribute this lab under the MIT license in LICENSE. Attribution or a backlink to a product is not a condition beyond retaining the license notice.

Expected result: the JSON report contains `"passed": 6`, `"total": 6`, and `"errors": []`. These counts are a reproducibility check, not a claim about rendering accuracy, production dimensions or cutting safety.
