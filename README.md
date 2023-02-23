<img width="1676" alt="image" src="https://user-images.githubusercontent.com/20548516/221004632-a31c71d6-0fa4-4a76-b578-06a51ebf85f0.png">

# sveltekit-modal-ocr

An example SvelteKit project using https://github.com/semicognitive/sveltekit-modal, showing how easy it is to write Python endpoints in SvelteKit.

See the code for the [example `+server.py` route here](src/routes/api/summarize/%2Bserver.py). You'll see it largely mirrors the SvelteKit built-in [`+server.js`](https://kit.svelte.dev/docs/routing#server)!

## This example 
- Includes a frontend written in [TailwindCSS](https://tailwindcss.com)
- Has a `api/ocr` endpoint which takes an image upload of a receipt, and does OCR on it! Inspired by the [Modal OCR example](https://modal.com/docs/guide/ex/doc_ocr_jobs)
