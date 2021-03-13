from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadVideo
from .forms import faderange
import moviepy.video.fx.all as vfx
from moviepy.editor import  *
from .forms import faderange2
from .forms import speedfactor
from .forms import volumefactor
from .forms import rotateangle
from .forms import gammavalue
# Create your views here.
def handle_uploaded_file(f):
 global vname
 vname = f.name
 with open('coralcut/static/'+f.name,'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def edit_video(request,*args):
 if request.method=="POST":
  form = UploadVideo(request.POST,request.FILES)
  if form.is_valid():
   handle_uploaded_file(request.FILES['video']) 
   return HttpResponseRedirect('/homepage/',{'form':form})
   
 else:
  form = UploadVideo()
  try: args ={'form':form,'vname':vname};print(vname)
  except: args = {'form':form};print("not global")
 return render(request,'coralpage.html',args)
 
def black(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.blackwhite,RGB=None, preserve_luminosity=True)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def paint(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.painting,saturation=1.5,black=0.009)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def fade_in(request):
 if request.method=="POST":
  form=faderange(request.POST,request.FILES)
  if form.is_valid():
   global vname
   Duration=form.cleaned_data['duration']
   Color=form.cleaned_data['color']
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.fx(vfx.fadein,duration=Duration,initial_color=Color)
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=faderange()
  try: maxrange=VideoFileClip("coralcut/static/%s"%(vname)).duration
  except:pass
  try:args={'form':form,'vname':vname,'maxrange':maxrange}
  except:
        try:args={'form':form,'vname':vname}
        except:
            try:args={'form':form}
            except:pass
 return render(request,'coralpage.html',args)
 
def fade_out(request):
 if request.method=="POST":
  form=faderange2(request.POST,request.FILES)
  if form.is_valid():
   global vname
   Duration=form.cleaned_data['duration2']
   Color=form.cleaned_data['color2']
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.fx(vfx.fadeout,duration=Duration,initial_color=Color)
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=faderange2()
  try: maxrange2=VideoFileClip("coralcut/static/%s"%(vname)).duration
  except:pass
  try:args={'form':form,'vname':vname,'maxrange2':maxrange2}
  except:
        try:args={'form':form,'vname':vname}
        except:
            try:args={'form':form}
            except:pass
 return render(request,'coralpage.html',args)
 
def mirrorx(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.mirror_x,apply_to="mask")
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def mirrory(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.mirror_y,apply_to="mask")
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def timesymmetry(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.time_symmetrize)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def invertcolors(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.invert_colors)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def lumcontrast(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.lum_contrast,lum=0,contrast=0,contrast_thr=127)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def evensize(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.even_size)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def timemirror(request):
 global vname
 myclip = VideoFileClip("coralcut/static/%s"%(vname))
 mynewclip = myclip.fx(vfx.time_mirror,self)
 mynewclip.write_videofile("coralcut/static/1%s"%(vname))
 vname="1%s"%(vname)
 return HttpResponseRedirect('/homepage/')
 
def speed(request):
 if request.method=="POST":
  form=speedfactor(request.POST,request.FILES)
  if form.is_valid():
   global vname
   Factor=form.cleaned_data['factor']
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.fx(vfx.speedx,factor=Factor,final_duration=None)
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=speedfactor()
  try:args={'form':form,'vname':vname}
  except:
   try:args={'form':form}
   except:pass
 return render(request,'coralpage.html',args)
 
def volume(request):
 if request.method=="POST":
  form=volumefactor(request.POST,request.FILES)
  if form.is_valid():
   global vname
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.volumex(form.cleaned_data['volfactor'])
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=volumefactor()
  try:args={'form':form,'vname':vname}
  except:
   try:args={'form':form}
   except:pass
 return render(request,'coralpage.html',args)
 
def rotate(request):
 if request.method=="POST":
  form=rotateangle(request.POST,request.FILES)
  if form.is_valid():
   global vname
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.add_mask().rotate(form.cleaned_data['degree'],unit="deg")
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=rotateangle()
  try:args={'form':form,'vname':vname}
  except:
   try:args={'form':form}
   except:pass
 return render(request,'coralpage.html',args)
 
def gammac(request):
 if request.method=="POST":
  form=gammavalue(request.POST,request.FILES)
  if form.is_valid():
   global vname
   Gamma=form.cleaned_data['gamma']
   myclip = VideoFileClip("coralcut/static/%s"%(vname))
   mynewclip = myclip.fx(vfx.gamma_corr,gamma=Gamma)
   mynewclip.write_videofile("coralcut/static/1%s"%(vname))
   vname="1%s"%(vname)
   return HttpResponseRedirect('/homepage/')
 else:
  form=gammavalue()
  try:args={'form':form,'vname':vname}
  except:
   try:args={'form':form}
   except:pass
 return render(request,'coralpage.html',args)