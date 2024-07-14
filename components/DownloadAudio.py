import fastapi

from AppCore import app, s3

@app.get("/download/{file}")
async def download_audio(
    file: str = fastapi.Path(
            description = "Download audio from S3 storage"
        )
):
    
    file_stream = s3.get_file("audio-host-store", file)

    file_stream = file_stream['Body'].iter_chunks()
    headers = {
        'Content-Disposition': f'attachment; filename="{file}"'
    }
    return fastapi.responses.StreamingResponse(file_stream, media_type='application/octet-stream', headers=headers)