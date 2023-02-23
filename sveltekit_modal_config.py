import modal

config = {
    'name': 'sveltekit-modal-ocr',
    'log': True,
    'stub_asgi': {
        'gpu': 'any',
        'shared_volumes': {
            '/root/model_cache': modal.SharedVolume().persist("doc_ocr_model_vol")
        },
        'image': modal.Image.debian_slim().pip_install("python-multipart", "donut-python==1.0.7", "transformers==4.21.3"),
        'secret': modal.Secret.from_name("my-openai-secret"),
        'retries': 3
    }
}