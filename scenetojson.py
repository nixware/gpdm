import Algorithmia #Importa a Biblioteca Algorithmia

input = {
    "video": "url",
    "detector": "content",
    "output_collection_frames": "scenecuts"
}

client = Algorithmia.client('sim0K+aJ2N+cJ+pP75A+dffnZGU1')
algo = client.algo('media/SceneDetection/0.1.6')
print algo.pipe(input)
