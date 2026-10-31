# Why does my SVG import at the wrong size? Check the page, units, and artwork separately

An SVG can have a correctly sized page and still contain artwork that is smaller than the size you expected. Before scaling everything until it looks right, separate three things: the document's physical dimensions, its internal coordinate system, and the extent of the actual drawing.

The repository includes a [physical-size fixture](../examples/size-physical.svg) and a [pixel-size fixture](../examples/size-pixels.svg). The physical-size file contains this complete example:

```svg
<svg xmlns="http://www.w3.org/2000/svg"
     width="100mm" height="60mm" viewBox="0 0 400 240">
  <rect x="10" y="10" width="380" height="220" fill="#21354a"/>
</svg>
```

The page is 100 mm wide and 60 mm high. The internal coordinate space is 400 by 240 units. The rectangle starts 10 units from each edge and occupies 380 by 220 units. It therefore measures 95 by 55 mm in that page, with a 2.5 mm margin on every side. A program reporting a 95 mm selected object has not necessarily imported the 100 mm page incorrectly.

## Start with the outer SVG element

Open a copy of the file in a text editor and find its outer `<svg>` element. Record `width`, `height`, and `viewBox`. You can inspect those attributes without changing the file.

`width` and `height` can specify physical dimensions. The four `viewBox` numbers describe the internal rectangle mapped into the viewport; they are not four measurements in millimetres. [MDN's viewBox reference](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox) explains this mapping.

In the example above, both rectangles have the same aspect ratio: 100:60 equals 400:240. One internal unit therefore represents 0.25 mm. Changing the `viewBox` to `0 0 100 60` without changing the drawing coordinates would change how the existing rectangle fits the page. It is not a harmless way to attach units.

If the file uses percentages, nested SVG elements, transformations, or stylesheets, use an editor to inspect the rendered result. This small example deliberately avoids those extra cases.

## Compare a pixel-sized version

Keep the same rectangle and `viewBox`, but change the outer attributes to `width="400" height="240"`. You have removed the explicit physical dimensions.

We loaded both versions into the live [Pic2SVG SVG cut-file checker](https://pic2svg.com/svg-cut-file-checker/) on 31 October 2026. The pixel-sized version reported 400 × 240 px and showed the following size interpretations:

| Interpretation | Page size |
| --- | --- |
| 96 pixels per inch | 105.8 × 63.5 mm |
| 72 pixels per inch | 141.1 × 84.7 mm |
| Explicit `100mm` × `60mm` version | 100 × 60 mm |

Those first two rows demonstrate why an implicit pixel-to-inch conversion matters. They are calculations displayed by the checker, not evidence that a particular current version of a cutting application uses either convention. Confirm the behavior of your actual importer.

Both files contained one closed rectangle and four nodes. Neither contained an embedded bitmap. The structural checks were similar, while their physical size declarations differed. A clean outline alone cannot settle the intended scale.

## Measure the object you need to make

After importing, select the drawing and read its width and height. Then check the page separately. If you need a 100 mm-wide rectangle from this example, changing the page label to 100 mm will not achieve that: it already has a 100 mm page and a 95 mm rectangle.

Set the object's required width in your editor with its aspect ratio locked, and check the other dimension. If both dimensions must match a specification, compare their ratio before resizing. An incompatible pair of dimensions requires distortion or a design change.

Export a fresh SVG, reopen that exported file, and measure again. For a handoff, include the intended object dimensions in plain language, such as “the outer rectangle should measure 95 × 55 mm.” This gives the receiving person a concrete check without relying on a thumbnail or filename.

The checker reads markup locally in the browser and accepts SVG files up to 2 MB. It does not measure a rendered design, resolve stylesheet rules or `<use>` clones, detect duplicate cutting geometry, or test a machine. Use its dimension report as an early check, then verify the imported object and make an appropriate material test before production.

## Disclosure and verification limits

Prepared with OpenAI Codex assistance on behalf of Pic2SVG. The two small SVG fixtures were checked in the live tool on 31 October 2026. The 95 × 55 mm object dimensions are arithmetic from the fixture, not a physical measurement. No physical cutting or third-party vector-editor/importer test was performed. The MIT license applies to files in this repository. It does not relicense separately hosted assets or services, or override third-party rights.
