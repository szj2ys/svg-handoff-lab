# My file ends in .svg, so why can't I edit the picture's outline?

Saving a picture inside an SVG document does not necessarily turn that picture into editable vector shapes. SVG can contain paths, text, and other objects, but it can also contain a raster image. The file extension tells you the container format; you still need to inspect what is inside it.

This matters when you need to move the nodes of a drawn outline, change individual regions, or supply paths for a cutting workflow. A photograph stored inside an SVG still has pixels. It may be useful for a print or engraving workflow, but the wrapper does not give the photograph a vector boundary.

## Look for an image object

Work on a copy. In your editor, inspect the object or layer type. If the visible picture is an image object, the editor may offer controls for the whole rectangle but no nodes along the pictured shape.

You can also open the SVG in a text editor. An `<image>` element points to an image through `href`, or through the older `xlink:href` spelling. That value can be a file URL or a data URI containing the image bytes. [MDN's SVG image documentation](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/image) confirms that this element can display raster files as well as other SVG documents. An `<image>` tag alone therefore warrants inspection; its referenced content determines what it contains.

Do not delete the image before you know whether it is the only visible artwork. A document can also mix a raster picture with useful vector annotations, a clipping shape, or a frame. Finding a single `<path>` somewhere in the file does not prove that the picture itself has been traced.

For a separate offline exercise, inspect this repository's [embedded-raster example](../03-embedded-raster.svg) and [mixed example](../04-mixed.svg). Those original teaching fixtures are separate from the public heart files used below.

## Compare two real, inspectable examples

We used the public [heart PNG](https://pic2svg.com/examples/batch/icon-heart.png) and [heart SVG](https://pic2svg.com/examples/batch/icon-heart.svg) available from Pic2SVG on 31 October 2026. For the first case, we placed the PNG bytes in an SVG `<image>` element as a data URI. For the second, we used the published SVG file directly.

Both files were selected in the live [SVG cut-file checker](https://pic2svg.com/svg-cut-file-checker/), and the check was run for each one:

| File inspected | Embedded bitmap result | Drawing result |
| --- | --- | --- |
| SVG wrapper containing the heart PNG | One bitmap | No drawing shapes outside definitions |
| Published heart SVG | No embedded bitmap | Two closed outlines, 38 nodes |

The published vector example also triggered a warning for a filled shape covering the canvas. Its page size was 160 × 160 px, without a physical unit. These details matter: having real paths does not mean the file is already prepared for every job.

The experiment tests file structure, not how closely the vector matches the original at every scale. It also does not prove that a cutter can reproduce the design. Readers can repeat the check with the linked public SVG; the hosted example may change in a future release.

## Choose the next step based on the job

If the artwork was originally created as vectors, ask for an export that preserves those objects. Tracing a screenshot of existing vector artwork discards information that the original file may still contain.

If the source really is a raster drawing, logo, or icon, tracing is a separate operation. Pic2SVG's hosted converter accepts raster files and produces filled vector paths using a deterministic tracing engine. Conversion uploads the image to its server; the local SVG checker does not. Keep that distinction in mind when deciding where to process confidential material.

A trace will need inspection. For example, a thick pen line can become a filled outline around the line rather than a single path down its centre. Fine texture and small lettering may need manual work. For artwork that must match an exact specification, compare the result against the source in a vector editor before using it.

After tracing, inspect the actual output again. Select the shapes, examine their nodes, check whether the file still contains image objects, and review unnecessary backgrounds or extra objects. Keep an editable source file as well as the exported SVG so later changes remain practical.

The local checker accepts SVG files up to 2 MB and reads their markup without rendering or uploading them. It does not resolve stylesheet rules or `<use>` clones, and it cannot identify every overlap or judge physical manufacturability. It helps answer the first useful question: does this file contain drawing shapes, a bitmap, or both? The next checks depend on what you intend to do with the artwork.

## Disclosure and verification limits

Prepared with OpenAI Codex assistance on behalf of Pic2SVG. The public heart files were checked on 31 October 2026. The SVG at that time was 643 bytes and contained two closed outlines/38 nodes; a future hosted version can differ. These are markup observations, not measurements of visual fidelity or physical output. No physical cutting or third-party vector-editor/importer test was performed. The MIT license applies to files in this repository. It does not relicense separately hosted assets or services, or override third-party rights.
