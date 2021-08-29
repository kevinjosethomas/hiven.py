from hiven.client import Client

class AttachmentSchema:
    media_url: str
    filename: str
    dimensions: dict


class Attachment:
    def __init__(self, attachment: AttachmentSchema, client: Client):
        self.media_url = attachment.media_url
        self.filename = attachment.filename
        self.dimensions = attachment.dimensions
