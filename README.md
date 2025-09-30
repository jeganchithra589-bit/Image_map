# Ex04 Places Around Me
# Date:30/09/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
<html>
    <title></title>
   <body>
    <center>
         
    <img src="Screenshot (19).png" usemap="#image-map">

<map name="image-map">
    <area target="_parent" alt="Tiruvannamalai" title="Tiruvannamalai" href="city.html" 
    coords="872,477,892,514" shape="rect">
    <area target="_parent" alt="Arunachala temple" title="Arunachala temple" href="temple.html" 
    coords="786,402,840,414" shape="rect">
    <area target="_parent" alt="MMCC" title="MMCC" href="ground.html" 
    coords="367,540,434,547" shape="rect">
    <area target="_parent" alt="Rajalakshmi engineering college" title="Rajalakshmi engineering college" href="college.html" 
    coords="1467,227,64" shape="circle">
    <area target="_parent" alt="IMAGICA Park" title="IMAGICA Park" href="park.html" 
    coords="840,142,64" shape="circle">


city.html:
<html>
    <title>Tiruvannamali</title>
    <body style="background:linear-gradient(to left,cyan);">
        <style>
            h1{
                font-family: 'Franklin Gothic Medium';
                font-size: medium;
                text-align:center;
                font-style:oblique;
            }
            img{
                border-radius:20px;
                margin:auto;
                display:block;
                image-rendering: auto;
                height:400px;
                width:600px;

            }
            p{
                text-align: left;
                font-style: italic;
            }
        </style>
        <h1 align="center">Tiruvannamali City</h1>
        <br><image src="Screenshot (60).png" usemap="#tiruvannamali"
        mapname="tiruvannamali"></br>
        
        <area shape="poly" align="center" alt="Tiruvannamlai" title="Tiruvannamalai">
        <p align="center" font-wieght="itallic">🛕 Religious & Spiritual Significance:

<h2>Annamalaiyar Temple:</h2>

A massive temple dedicated to Lord Shiva (as Arunachaleswarar).
One of the Pancha Bhoota Sthalams, representing the element Fire (Agni).
Known for its grand Rajagopurams (gateway towers), each richly sculpted.
<h3>Girivalam / Pradakshina:</h3>

Devotees walk 14 km around Arunachala Hill, especially on full moon nights.
Believed to cleanse sins and bring spiritual progress.

Karthigai Deepam Festival:

The most important festival celebrated annually.
A giant flame (Deepam) is lit on top of Arunachala Hill, visible for miles, symbolizing Lord Shiva’s cosmic light.</p>
    </body>
</html>


college.html:

<!DOCTYPE html>
<html>
    <head>
    <title></title>
    </head>
    <body style="background:linear-gradient(to left,rgb(0, 255, 81));">
        <style>
            h1{
                font-family:bold;
                text-align: center;
                background-clip:aqua;
                font-style:italic;
            }
            img{
                border-radius: 20px;
                box-shadow:inset;
                margin:auto;
                display:block;
            }
            p{
                font-family: 'Lucida Sans';
                font-size: medium;
                font-style: oblique;
            }
        </style>
        <h1>Rajalakshimi Polytechnic college</h1>
        <img src="Screenshot (58).png" align="center" font-color="red">
        <p>Rajalakshmi Polytechnic College, was established in 2008 in Tiruvannamalai, Tamil Nadu. 
            It is a private institute approved by AICTE. The institute offers Diploma programme in Full Time mode. It offers a total of 7 courses in 6 specializations including Civil Engineering, 
            Electronics & Communication Engineering, Electronics Engineering, Mechanical Engineering, Automobile Engineering and Tool Engineering. 
            The course offered at Rajalakshmi Polytechnic College include After 10th Diploma. 
            The total seat intake for the available courses is 420. Rajalakshmi Polytechnic College offers courses across stream such as Engineering. 
            The institute offers all the necessary facilities to the students.</p>
    </body>
</html>


ground.html:

<html>
    <title></title>
    <body style="background:linear-gradient(to left,rgb(26, 0, 128),cyan,rgba(0, 255, 30, 0.596));">
        <style>
            h1{
                text-align: center;
                font-style: italic;
                font-size: larger;
            }
            img{
                border-radius:20px;
                display:block;
                margin:auto;
                height: 400;
                width:600;
            }
            p{
                font-style: oblique;
        
            }

        </style>
        <h1 align="center" font-size="medium">MMNC Ground</h1>
        <img src="Screenshot (61).png" align="center" font-size="medium">
        <p>The Tiruvannamalai MMNC Ground is a sports and fitness center located in Pandithapattu, Tiruvannamalai, known as Mmcc Cricket Ground. It is a 24-hour facility offering a variety of fitness classes, including cardio, strength training, and yoga. 
<h1>Key details: <h1>
Name: Mmcc Cricket Ground
Location: Pandithapattu, Tiruvannamalai - 606603
Operating Hours: Open 24 hours, every day of the week
Services: Provides a range of fitness classes and a comprehensive fitness experience for members.
tiruvannamalai mmnc ground
There are no search results for a specific "MMNC ground" in Tiruvannamalai. However, multiple search results point to a "Government Tiruvannamalai Medical College and Hospital" in Vengikkal, which may be the ground you are looking for. 
Location and potential misspellings
Medical college ground:
 The Government Tiruvannamalai Medical College and Hospital is located in the Vengikkal New Town area of Tiruvannamalai. It's possible the "MMNC ground" you're referring to is a recreational area or open space associated with this large institution.
Likely spelling variation: Some sources refer to a "Mmcc Cricket Ground" in the Pandithapattu area, though it is not specified if this is a large, public-use ground. It is a possible misspelling of MMNC.
Other grounds: Other private cricket and sports grounds exist in the district, such as Cheyyar College Play Ground and Blue Diamond Cricket Ground.

        </p>
    </body>
    
</html>


park.html:


<html>
    <title></title>
    <body style="background:linear-gradient(to left,rgb(26, 0, 128),cyan,rgba(0, 255, 30, 0.596));">
        <style>
            h1{
                text-align: center;
                font-style: italic;
                font-size: larger;
            }
            img{
                border-radius:20px;
                display:block;
                margin:auto;
                height: 400;
                width:600;
            }
            p{
                font-style: oblique;
        
            }

        </style>
        <h1 align="center" font-size="medium">MMNC Ground</h1>
        <img src="Screenshot (61).png" align="center" font-size="medium">
        <p>The Tiruvannamalai MMNC Ground is a sports and fitness center located in Pandithapattu, Tiruvannamalai, known as Mmcc Cricket Ground. It is a 24-hour facility offering a variety of fitness classes, including cardio, strength training, and yoga. 
<h1>Key details: <h1>
Name: Mmcc Cricket Ground
Location: Pandithapattu, Tiruvannamalai - 606603
Operating Hours: Open 24 hours, every day of the week
Services: Provides a range of fitness classes and a comprehensive fitness experience for members.
tiruvannamalai mmnc ground
There are no search results for a specific "MMNC ground" in Tiruvannamalai. However, multiple search results point to a "Government Tiruvannamalai Medical College and Hospital" in Vengikkal, which may be the ground you are looking for. 
Location and potential misspellings
Medical college ground:
 The Government Tiruvannamalai Medical College and Hospital is located in the Vengikkal New Town area of Tiruvannamalai. It's possible the "MMNC ground" you're referring to is a recreational area or open space associated with this large institution.
Likely spelling variation: Some sources refer to a "Mmcc Cricket Ground" in the Pandithapattu area, though it is not specified if this is a large, public-use ground. It is a possible misspelling of MMNC.
Other grounds: Other private cricket and sports grounds exist in the district, such as Cheyyar College Play Ground and Blue Diamond Cricket Ground.

        </p>
    </body>
</html>

temple.html:

<!DOCTYPE html>
<html>
    <title></title>
    <body style="background:linear-gradient(to left,rgb(128, 58, 0),rgb(255, 119, 0),rgb(0, 255, 200));">
    <style>
        img{
            align-items: center;
            text-align: center;
            display:block;
            margin:auto;
            border-radius:10px;
            height: 300px;
            width:600px;
        }
        caption{
            text-align: center;
            font-size:bold;
            font-family:aqua;
            font-style:italic;
            font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif

        }
        p{
         text-align: center;
         font-weight:200;
         font-weight:200px;
         font-style: italic;

        }
        </style>
        <caption><h1 align="center" font-wieght="bold">Arunachala Temple</h1></caption>
        
        <img src="Screenshot (56).png" align="center" >
        
<p><h1>Key Aspects:</h1>

Deity:
The temple is dedicated to Lord Shiva, who is represented by the Agnilingam. 
Location:
 It is situated at the base of the Anamalai Hills, from which it gets its name. 
Architecture and Size:
 The temple is a vast complex, one of the largest in India, featuring beautiful sculptures, intricate carvings, and massive gopurams (ent towers). 
Historical Significance:
 Its history spans centuries, with architectural contributions from various dynasties including the Cholas, Pandiyas, and Vijayanagar kings. It is mentioned in the 7th-century Tamil work Thevaram. 
Karthigai Deepam Festival:
 The temple is the site of the popular Karthigai Deepam festival, an ancient and widely celebrated festival. 
Legend of the Pillar of Fire: A central myth tells of a conflict between Brahma and Vishnu, leading Shiva to manifest as an enormous pillar of fire (the Agnilinga) and challenge them to find its beginning or end.</p>
Unique Features:
Giri Pradakshina: 
The temple is associated with the popular religious practice of Giri Pradakshina, a circumambulation of the sacred Arunachala Hills.
Numerous shrines: The complex contains several smaller shrines, including one dedicated to Goddess Unnamalaiyar, his wife, and another for the nine planets (Navagrahas).</p>
    </body>
</html>


```
# OUTPUT
![alt text](<Screenshot (65).png>)
![alt text](<Screenshot (66).png>)
![alt text](<Screenshot (67).png>)
![alt text](<Screenshot (68).png>)
![alt text](<Screenshot (69).png>)
![alt text](<Screenshot (70).png>)
# RESULT
The program for implementing image maps using HTML is executed successfully.
