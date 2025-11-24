from django.db import models
from django.contrib.auth.models import User



# Создаем таблицу в базе данных и ее колонки
class Category(models.Model):
    #Сохдание колоннок в таблице
    name = models.CharField(max_length=20) # создание Str поля с ограничением символов
    description = models.TextField(blank=True) # Создание Str поля большого количества текста

    #магическим метод str для получения строки из обьекта
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
            return self.name
        
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    updete_at = models.DateTimeField(auto_now=True)


    # One-to-Many - один автор много постов 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #ForeignKey связь одтн ко многим 
    #on_delete=models.CASCADE - При удаление родителя удаляеться доченирнеи записи 

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    #on_delete=models.SET_NULL,null=True - при удаление родителя поле просто становиться NULL
    #Many-to-Many

    tegs = models.ManyToManyField(Tag,blank=True) 

    def __str__(self):
         return self.title
    
class Comment(models.Model):
     post = models.ForeignKey(Post,on_delete=models.CASCADE)    
     author = models.ForeignKey(User,on_delete=models.CASCADE)
     text = models.TextField()
     creat_at = models.DateTimeField(auto_now_add=True)
     updete = models.DateTimeField(auto_now=True)

     def __str__(self):
          return f"Коментарий от {self.author} для {self.post}"
     
        

