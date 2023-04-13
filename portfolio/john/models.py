from django.db import models

#home page

class home(models.Model):
    name = models.CharField(max_length=20)
    greetingTop = models.CharField(max_length=20)
    greetingBottom = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='homePicture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#about me

class aboutMe(models.Model):
    header = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profileImage = models.ImageField(upload_to='profilePicture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.occupation


#links

class links(models.Model):
    about = models.ForeignKey(aboutMe, on_delete=models.CASCADE)
    socialName = models.CharField(max_length=20)
    socialLink = models.URLField(max_length=200)



#skills

class category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class skills(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    skillName = models.CharField(max_length=20)


#portfolio

class portfolio(models.Model):
    image = models.ImageField(upload_to='portfolioPicture/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'