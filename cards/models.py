from django.db import models

# Create your models here.

box_num=5 #Number of Boxes
BOXES=range(1 , box_num+1)

class Card(models.Model):
    
    question=models.CharField(("Question"), max_length=100)
    answer=models.CharField(("Answer"), max_length=100)    
    box=models.IntegerField(("Box_number"),choices=(zip(BOXES,BOXES)),default=BOXES[0])
    date_created=models.DateField(("created_on"), auto_now_add=True)  
    
    def __str__(self) -> str:
        return self.question
    
    def move(self,correct):
        
        new_box=self.box+1 if correct else BOXES[0]
        
        if new_box in BOXES:
            self.box=new_box
            self.save() #mandatory 
        
        # if correct:
        #     if self.box==box_num:
        #         self.box=BOXES[0]
        #     else:
        #         self.box=self.box+1
        # else:
        #     if self.box == BOXES[0]:
        #         self.box=BOXES[0]
        #     else:
        #         self.box=self.box-1