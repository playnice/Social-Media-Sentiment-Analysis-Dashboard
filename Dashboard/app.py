import pygal
from pygal.style import Style
import pandas as pd
from flask import Flask, Response, url_for

app = Flask(__name__)

@app.route('/')
def index():
	""" render svg on html """
	return """
<html>
<head>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</head>
<style>
	.Container{
		width: 1200px;
		height: 200px;
		float: left;
	}

	.styled-select select{
	   background: white;
	   border-radius: 25px;
	   font-size: 14px;
	   margin: 10px;
	   height: 29px;
	   width: 268px;
	}

	body{
	}
	
	.boxt {
		background:#FFF;
		border-radius: 25px;
	}
	.effectt{
		 #box-shadow: 0 10px 6px -6px #777;
	}
	
	.box{
		background:#FFF;
		width: 1330px;
		height: 500px;
		margin: 10px;
		float: left;
		border: 1px solid black;
		border-radius: 25px;
	}
	.effect1{
		 box-shadow: 0 10px 6px -6px #777;
	}
	.insideBox{
		width: 650px;
		height: 650px;
		margin:auto;
		float: left;
	}
	.insideBox2{
		width: 220px;
		height: 220px;
		float: left;	
	}
	.besideBox{
		margin:10px;
		min-width:380px;
		height:220px;
	}
	.aspect{
		margin:7px;
	}
	.imgclass{
		width: 1330px;
		height: 1360px;
		margin: 10px;
		float: left;
		border: 1px solid black;
		border-radius : 25px;
		box-shadow: 0 10px 6px -6px #777;
	}	
	.imgclass2{
		width: 1330px;
		height: 750px;
		margin: 10px;
		float: left;
		border: 1px solid black;
		border-radius : 25px;
		box-shadow: 0 10px 6px -6px #777;
	}
	
	.instagram{
		font-size:24px;
		font-weight: bold;
	}
</style>
<body>
<div class = "Container">
	<div class = "boxt effectt" style = "float: left;"><img src="/static/hhlogo.jpg" alt="HahaNoYume" width="450px" height="210px"></div>	
	<br>
	<div class = "f" style = "float: left;">&emsp;&emsp;&emsp;<img src="/static/facebook.png" alt="Facebook logo" width="150px" height="150px"></div>
	<div class = "fw" style = "float: left;"><br><br><h6>6,427 likes  <img src="/static/like.png" alt="like" width="20px" height="20px"><br>6,477 followers  <img src="/static/follower1.png" alt="like" width="18px" height="18px"></h6></div>
	<div class = "i" style = " float: left; margin-top: 15px"><img src="/static/instagram.jpg" alt="Instagram logo" width="150px" height="120px"></div>
	<div class = "iw" style = "float: left; "><br><br><h6>237 posts  <img src="/static/post.png" alt="like" width="20px" height="20px"><br>9,644 followers  <img src="/static/followers.png" alt="like" width="30px" height="30px"></h6></div>
	<br>
	<br>
</div>

<div class = "box effect1">
	<div class = "insideBox">
		<figure>
			<embed type="image/svg+xml" src="/reactionDistribution/" />
		</figure>
	</div>
	<div class = "insideBox">
		<figure>
			<embed type="image/svg+xml" src="/sentimentRatioComment/" />
		</figure>
	</div>
</div>

<div class = "box effect1">
	<div class = "insideBox">
		<figure class = "aspect">
			<embed type="image/svg+xml" src="/aspectSentiment/" />
		</figure>
	</div>
	<div class = "insideBox">
		<figure>
			<embed type="image/svg+xml" src="/likeGrowth/" />
		</figure>
	</div>
</div>

<div class = imgclass>
<div align = center>
	<img src="/static/CommentWordCloud.png" alt="HahaNoYume" width="650px" height="650px">
</div>
<h3> &nbsp;Positive & Negative Sentiment WordCloud</h3>
	<img class = "aspect" src="/static/Positivehahanoyume.png" alt="HahaNoYume" width="640px" height="650px">
	<img class = "aspect" src="/static/Negativehahanoyume.png" alt="HahaNoYume" width="640px" height="650px">
</div>
<div class = imgclass2>	
<h3>  &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;Instagram Network Graph  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Top 3 Influencers</h3>
	<div class = "insideBox">
		<img class = "aspect" src="/static/insta-network-whole.png" alt="HahaNoYume" width="640px" height="650px">
	</div>	
	<div class = "insideBox">
		<div class = "insideBox2">
			<a href = "https://www.instagram.com/cecelianewyork/">
			<img class = "aspect" src="/static/influ1.jpg" alt="cecelianewyork" width="210px" height="210px">
			</a>
		</div>	
		<div class = "besideBox">
			<br>
			<span class = "instagram">cecelianewyork</span>
			<br><br>
			<b>962</b> posts &nbsp;&nbsp; <b>36.7k</b> followers  &nbsp;&nbsp;<b>2,704</b> following
			<br><br>Cecelia New York Shop link in bio Share with us <a href = "https://www.instagram.com/explore/tags/ceceliainthecity/">#ceceliainthecity</a>
			<a href = "https://cecelianewyork.com/">www.cecelianewyork.com</a>
		</div>
		<div class = "insideBox2">
			<a href = "https://www.instagram.com/my.pomeranian.guests/">
			<img class = "aspect" src="/static/influ2.jpg" alt="iamlivrose" width="210px" height="210px">
			</a>
		</div>	
		<div class = "besideBox">
			<br>
			<span class = "instagram">my.pomeranian.guests</span>
			<br><br>
			<b>527 </b> posts &nbsp;&nbsp; <b>16.9k</b> followers  &nbsp;&nbsp;<b>5,673</b> following
			<br><br><b>Alla:</b> Spitz ( pomeranian, german) for sale. Delivery. All documents . From St-Petersburg, RU . +7-965-771-86-88(Viber.WhatsApp, FT)
		</div>	
		<div class = "insideBox2">
			<a href = "https://www.instagram.com/iamlivrose/">
			<img class = "aspect" src="/static/influ3.jpg" alt="my.pomeranian.guests" width="210px" height="210px">
			</a>
		</div>		
		<div class = "besideBox">
			<br>
			<span class = "instagram">iamlivrose</span>
			<br><br>
			<b>469 </b> posts &nbsp;&nbsp; <b>34.7k</b> followers  &nbsp;&nbsp;<b>3,921</b> following
			<br><br><b>LIV KNIGHT-BUTLER</b> 22 | London | Mummy to Reggie 👶🏽🖤 - 07/09/17
			<a href = "www.youtube.com/channel/UCGzRsKjnbjhzewTXuVaTVpw">www.youtube.com/channel/UCGzRsKjnbjhzewTXuVaTVpw</a>
		</div>
	</div>
</div>
</body>
</html>
"""

@app.route('/reactionDistribution/')
def reactionDistribution():
	data = pd.read_csv('reactions6months.csv',header = None)
	custom_style = Style(
	font_family ='googlefont:Raleway',
	title_font_family ='Arial Black',
	title_font_size = 20,
	label_font_size = 16,
	tooltip_font_size = 16,
	  background ='transparent',
	  foreground ='black',
	  foreground_strong='black',
	  foreground_subtle='#630C0D',
	  opacity='.6',
	  opacity_hover='.9',
	  transition='400ms ease-in',
	  colors=( '#0000FF','#ff0000')
	  )
	hbar_chart = pygal.HorizontalBar(show_legend=False, style= custom_style)
	hbar_chart.title = 'Reaction Distribution of 6 months'
	reaction_list = []
	reaction_list.append(int(data.iloc[1,1]))
	reaction_list.append(int(data.iloc[2,1]))
	reaction_list.append(int(data.iloc[3,1]))
	reaction_list.append(int(data.iloc[4,1]))
	reaction_list.append(int(data.iloc[5,1]))
	
	hbar_chart.add('',reaction_list)
	hbar_chart.x_labels = 'Angry', 'Sad', 'Wow','Haha','Love'
	hbar_chart.x_title = 'Count'
	hbar_chart.y_title = 'Reaction Type'
	return Response(response=hbar_chart.render(), content_type='image/svg+xml')


@app.route('/aspectSentiment/')
def aspectSentiment():
	custom_style = Style(
	font_family ='googlefont:Raleway',
	title_font_family ='Arial Black',
	title_font_size = 20,
	label_font_size = 16,
	tooltip_font_size = 16,
	  background ='transparent',
	  foreground ='black',
	  foreground_strong='black',
	  foreground_subtle='#630C0D',
	  opacity='.6',
	  opacity_hover='.9',
	  transition='400ms ease-in',
	  colors=('#ff0000','#0000FF')
	  )
	line_chart = pygal.HorizontalBar(show_legend=False,style = custom_style)
	line_chart.title = 'Aspect and its Sentiment'
	line_chart.x_labels ='QUALITY','KIMONO','PACKAGING','SERVICE','SHOP','BOX','ROMPER','MATERIAL','WORKMANSHIP','PACKAGE','ORDER','FABRIC','CUSTOMER SERVICE'
	line_chart.x_title = 'Sentiment Ratio'
	line_chart.y_title = 'Aspect'
	line_chart.add('Negative', [8.11/(48.65+8.11),18.18/(18.18+42.42),11.76/(11.76+17.65),5.56/(5.56+38.89),0.0				,0.0	  , 8.7/(8.7+56.52),0.0			,0.0		,0.0		,8.33/(8.33+41.67),16.67/(16.67+50),16.67/(16.67+33.33)])
	line_chart.add('Positive', [48.65/(48.65+8.11),42.42/(18.18+42.42),17.65/(11.76+17.65),38.89/(5.56+38.89), 46.67/46.67,71.43/71.43, 56.52/(8.7+56.52),77.78/77.78,33.33/33.33,55.56/55.56,41.67/(8.33+41.67),50.0/(16.67+50),33.33/(16.67+33.33)])
	return Response(response=line_chart.render(), content_type='image/svg+xml')

@app.route('/likeGrowth/')
def likeGrowth():	
	custom_style = Style(
	font_family ='googlefont:Raleway',
	title_font_family ='Arial Black',
	title_font_size = 20,
	label_font_size = 16,
	tooltip_font_size = 16,
	  background ='transparent',
	  foreground ='black',
	  foreground_strong='black',
	  foreground_subtle='#630C0D',
	  opacity='.6',
	  opacity_hover='.9',
	  transition='400ms ease-in',
	  colors=( '#0000FF','#ff0000')
	  )
	date_chart = pygal.Line(x_label_rotation=90, show_legend = False,style = custom_style)
	date_chart.x_labels = ['2017-11-27','2017-11-28','2017-11-29','2017-11-30','2017-12-01','2017-12-02','2017-12-03',
							'2017-12-04','2017-12-05','2017-12-06','2017-12-07','2017-12-08','2017-12-09','2017-12-10',
							'2017-12-11','2017-12-12','2017-12-13','2017-12-14','2017-12-15','2017-12-16','2017-12-17',
							'2017-12-18','2017-12-19','2017-12-20','2017-12-21','2017-12-22','2017-12-23','2017-12-24',
							'2017-12-25','2017-12-26']
	date_chart.title = 'Likes Growth from 27th Nov to 26 Dec 2017'
	date_chart.x_title = 'Date'
	date_chart.y_title = 'Likes Count'	
	date_chart.add("Likes", [5996,6004,6013,6030,6041,6059,6066,6072,6081,6092,6099,6104,6122,6118,6121,6129,6125,6127,
								6128,6130,6131,6132,6136,6137,6138,6138,6140,6146,6147,6149])
	return Response(response=date_chart.render(), content_type='image/svg+xml')

@app.route('/sentimentRatioComment/')
def sentimentRatioComment():
	custom_style = Style(
	font_family ='googlefont:Raleway',
	title_font_family ='Arial Black',
	title_font_size = 20,
	label_font_size = 16,
	tooltip_font_size = 16,
	  background ='transparent',
	  foreground ='black',
	  foreground_strong='black',
	  foreground_subtle='#630C0D',
	  opacity='.6',
	  opacity_hover='.9',
	  transition='400ms ease-in',
	  colors=( '#0000FF','#ff0000')
	  )
	data = pd.read_csv('Total_Sentiment_C.csv',header = None)
	pie_chart = pygal.Pie(show_legend=False, style=custom_style, inner_radius=.4)
	pie_chart.title = 'Total Sentiment of Comment'
	reaction_list = []
	reaction_list.append(int(data.iloc[2,1]))
	reaction_list.append(int(data.iloc[3,1]))
	pie_chart.add('Positive', reaction_list[0])
	pie_chart.add('Negative', reaction_list[1])
	return Response(response=pie_chart.render(), content_type='image/svg+xml')
	

if __name__ == '__main__':	
	app.run()