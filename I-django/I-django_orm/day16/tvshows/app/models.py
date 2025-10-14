from django.db import models

class TvShowManager(models.Manager):
    def add_show_validator(self, postData):
        errors = {}
        
        if 'title' not in postData or len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        
        if 'network' not in postData or len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        
        if 'release_date' not in postData or not postData['release_date']:
            errors["release_date"] = "Release date is required"
        else:
            import re
            date_regex = r"^\d{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01])$"
            if not re.match(date_regex, postData['release_date']):
                errors["release_date"] = "Release date must be in format YYYY-MM-DD"
        
        if 'description' in postData and postData['description'] and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters if provided"
        
        return errors
class TvShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManager()

    def __str__(self):
        return self.title




def add_show(postData):
    print(postData)
    tvShow= TvShow.objects.create(title=postData['title'], network=postData['network'], release_date=postData['release_date'], description=postData['description'])
    return tvShow
def get_show(id):
    return TvShow.objects.get(id=id)
def update_show(id, postData):
    tvShow = get_show(id)
    tvShow.title = postData['title']
    tvShow.network = postData['network']
    tvShow.release_date = postData['release_date']
    tvShow.description = postData['description']
    tvShow.save()
    return tvShow
def delete_show(id):
    tvShow = get_show(id)
    tvShow.delete()

def get_shows():
    return TvShow.objects.all()
# def edit_show(postData):

    
