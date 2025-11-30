Amid all this hype of AI, one needs to take a breath and know exactly what AI is. 

Humans have long dreamed of machines that can think. AI began traditionally in the 1940s with basic rule-based methods and today has evolved to unparalleled levels. I still remember my teacher saying in 2005, "Japanese scientists are
wasting millions of dollars every year on these useless robotics AI projects," and he was right. 

It's hard to believe that just a couple of years ago, AI was a highly ambitious field (they used to make sci-fi movies about it; I remember watching [Spielberg's movie in 2004](https://en.wikipedia.org/wiki/A.I._Artificial_Intelligence)). 
In 2003, I used the  Eliza chatbot (which had a memory like me and couldn't remember even a history of 3 messages) and more or less consigned myself to the fact that "that's that". AI is not going to progress beyond that.

In 2009, I graduated and still AI was just rule-based things, a couple of search methods, or a little bit of neural networks (very basics). I remember we made a doctor chatbot for our AI lab and it was just if conditions (in Prolog).

**Deep Learning**

In 2011/12, [AlexNet](https://en.wikipedia.org/wiki/AlexNet) was introduced and that was a revolution as it brought these computer vision-based models to a new level with much better accuracy. And floodgates broke soon afterwards, with a lot of progress in AI. Two of the most significant models were ResNets and Transformers.

> I know these names would look pretty alien/weird to you, but I wanted to mention **transformers** here as they enabled chatGPT and all these LLMs. Transformers were introduced in 2017 and as you can see, they brought a revolution within a few years.

---

I always like the historical aspect of things, hence mentioned it a bit here. Now, I will resume by redrawing the picture I drew in class.

<img width="749" height="695" alt="Screenshot 2025-11-30 at 5 50 06 PM" src="https://github.com/user-attachments/assets/338b7421-048f-4885-897d-a79ad928c5a9" />

(Image Credits: [Deep Learning, Ian Goodfellow](https://www.deeplearningbook.org/contents/intro.html))

This is a fundamental image and is equally important to both beginners in the field and seasoned practitioners. I would give some examples:

1. **Traditional AI:** A system you make using simple rules (i.e. if-else conditions) is a good example of traditional AI. The reason why computers were able to defeat even players like Gray Kasparov (and as early as 90s) was the ease of designing the rules for chess. There will be a lot of rules for chess, but they can be written down as an if-else code (even you can make it) and it's true for many other computer games too – even today. You can even make a program to classify an email as spam or normal by using simple rules. Traditional rule-based AI is very fast and hence still deployed in some real-time systems (Israel's Iron-Dome is a good example).
2. **Machine Learning:** Machine Learning necessarily involves learning. Your program is given some data to learn patterns and then uses it to create a model. Once we are satisfied with the model (usually by its accuracy), we can use it for our problems.
3. **Deep Learning:** DL models use neural networks with a lot of layers (hence deep). They allow us to use a lot of data (the reason why chatGPT and other LLMs weren't available prior to transformers was the inability of existing methods to take in a lot of data and use it) and hence take more computation (often GPUs for training) and better accuracy. Since deep models involve a lot of layers, hence understanding them is quite hard and challenging (example: chatbots' hallucinations).

> There is a difference between training a model (learning) and using it. The models we are using on HuggingFace etc are pre-trained models and we are just using them, not training them.

## Machine Learning

Now, I will turn my attention to the core of AI: machine learning. Machine learning can be loosely divided into two types:

### 1. Supervised Learning

In supervised learning, we give some data (usually denoted as $X$) and its labels (usually $Y$) to the program and the model uses them to learn. For example, I have a lot of images and also their labels (whether it's a person, car, airplane, clouds or whatever). After training the model, a good model will be able to identify a new image as a person portrait or a car or scenery, etc. This is precisely what happened in the ML models trained by Apple or Google. Once trained, they are now deployed on our phones and can easily classify objects in our gallery.

### 2. Unsupervised Learning

For unsupervised learning, we don't give any labels to the data. We say to the model: This is data, go and learn whatever you can. For example, we feed an unsupervised learning model with some images in our phone gallery (just images, no labelling). You can see it will automatically group related items: as scenaries will pretty much be grouped under one class, portraits under another one and so on.

### Classification and Regression

An ML model always predicts the input data. If that prediction is some number, it's a **Regression** model; otherwise, it's a **Classification** model.

Some examples will better elaborate on it.

1. Score-predictor in Cricket: Regression
2. Weather's temperature predictor: Regression
3. Covid test system: Classification

---

## ML Models

There are a number of ML models. But if you understand just a couple of them, you can understand half of the ML already. Let's begin with the first one.

### Linear Regression

Regression word may give you a mini _Deja vú_. Yes, regression models output a numerical value. Let's suppose we have data of some flights (distance vs time). You guys know that distance and time are directly proportional, which means if we draw a line between them in Excel, it will be something like a straight line.


A straight line can easily be represented by its equation, $y = mx+c$. If we know the values of $m$ and $c$, we can easily input any value of $x$ and can get the resulting value of $y$. If we go back to our example, it means that we can enter the value of any flight's distance (distance was $x$) and we can get its flight time.

For example, if we have the line's equation, say $y = 0.12x-23$ and a flight distance of [2338km](https://www.distance.to/LHE/DOH), then flight time will be 280-23=257 mins (4hrs 17mins).

But here's the ultimate question: **how to find $m$ and $c$?** Should we just hit-and-trial? Or is there some proper method too?

Luckily, there's one and I will teach it in the class this week. Also, please have a look at the Jupyter notebook I have just uploaded.

