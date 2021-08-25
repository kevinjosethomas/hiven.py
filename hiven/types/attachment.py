from ..schemas import Attachment


class Attachment:
    def __init__(self, attachment: Attachment):
        self.media_url = attachment.media_url
        self.filename = attachment.filename
        self.dimensions = attachment.dimensions
