import fastapi

from AppCore import app, s3

@app.get("/audio/{file}")
async def steam_audio(
        file: str = fastapi.Path(
            description = "Stream audio from S3 storage"
        )
    ):
    
    s3_response = s3.get_file("audio-host-store", file)

    if not s3_response:

        return fastapi.responses.Response("Source not found", status_code=404)

    def iterfile():
        stream = s3_response['Body']
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            yield chunk

    return fastapi.responses.StreamingResponse(iterfile(), media_type="audio/mp3")
