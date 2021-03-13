from django import forms

class UploadVideo(forms.Form):
 video = forms.FileField()

class faderange(forms.Form):
 duration= forms.IntegerField()
 color=forms.IntegerField()
 
class faderange2(forms.Form):
 duration2= forms.IntegerField()
 color2=forms.IntegerField()
 
class speedfactor(forms.Form):
 factor=forms.IntegerField()
 
class volumefactor(forms.Form):
 volfactor=forms.IntegerField()
 
class rotateangle(forms.Form):
 degree=forms.IntegerField()
 
class gammavalue(forms.Form):
 gamma=forms.IntegerField()