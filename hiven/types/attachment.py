class AttachmentSchema:
    media_url: str
    filename: str
    dimensions: dict


class Attachment:
    def __init__(self, attachment: AttachmentSchema, client):
        self.media_url = attachment.get("media_url")
        self.filename = attachment.get("filename")
        self.dimensions = attachment.get("dimensions")
