from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None
        
        if timestamp is None:
            self.timestamp = datetime.utcnow()
        else:
            self.timestamp = timestamp
        self.formatted_time = self.timestamp.strftime("%A, %b %d, %Y")
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
    def __str__(self):
        return ('@{first} {last}: "{post}"\n\t{timestamp}'.format(first=self.user.first_name, 
        last=self.user.last_name, post=self.text, timestamp = self.formatted_time))
        
# '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        super(PicturePost, self).__init__(text, timestamp)

    def __str__(self):
        return ('@{first} {last}: "{post}"\n\t{url}\n\t{timestamp}'.format(first=self.user.first_name, 
        last=self.user.last_name, post=self.text, url=self.image_url, timestamp=self.formatted_time))
# '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        super(CheckInPost, self).__init__(text, timestamp)

    def __str__(self):
        return ('@{first} Checked In: "{post}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(first=self.user.first_name, 
        last=self.user.last_name, post=self.text, latitude=self.latitude, longitude=self.longitude, timestamp = self.formatted_time))


# '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'