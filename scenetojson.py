import Algorithmia #Importa a Biblioteca Algorithmia

input = {
    "video": "url",
    "detector": "content"
    "output_collection_frames": "scenecuts"
}

client = Algorithmia.client('token')
algo = client.algo('media/SceneDetection/0.1.6')
print algo.pipe(input)
