from ctypes import Array
from datetime import datetime
from hashlib import md5

from pydantic import BaseModel

class NewsItemModel(BaseModel):
    url_hash: str
    title: str
    url: str
    text: str
    author: str
    date: datetime

class NewsItemSummaryModel(BaseModel):
    url_hash: str
    title: str
    url: str
    author: str
    date: datetime


class NewsItem:
    def __init__(self, url: str, title: str, text: str, author: str, date: datetime):
        self.url_hash = md5(url.encode()).hexdigest()
        self.title = title
        self.text = text
        self.url = url
        self.author = author
        self.date = date

        self.image = None
        # self.description = ""
        self.tags = []
    
    def as_model(self) -> NewsItemModel:
        return NewsItemModel(
            url_hash=self.url_hash,
            title=self.title,
            url=self.url,
            text=self.text,
            author=self.author,
            date=self.date
        )
    
    def as_summary_model(self) -> NewsItemSummaryModel:
        return NewsItemSummaryModel(
           url_hash=self.url_hash,
            title=self.title,
            url=self.url,
            author=self.author,
            date=self.date
        )


seed_data = [
    NewsItem(
        title="Code:{ish} the art of teaching computing!",
        url="https://www.computingatschool.org.uk/news-and-blogs/2022/october/codeish-the-art-teaching-computing",
        author="Stuart Ball | Chief Content Editor - Computing at School ",
        date=datetime(2022, 10, 5),
        text="""Speaking with an eminent colleague at CAS recently, we got to talking about CAS and its roots and how it has progressed. The discussion led to what is it we want to support teachers with? Is it professionalism, meeting the goals that all young people should have access to a world class computing education? Or is it Technical skills, how to do this, instructions and manuals of how to teach, assess and monitor that subject learning is taking place? Or finally the craft of teaching, the ideas and activities that make the subject exciting to teach and learn.

With the NCCE we have certainly developed the professionalism aspect, with teachers trained to develop and implement a  world-class computing education for all young people. We are spoilt for choice when it comes to Technical Skills, the CAS resources Library is full of these. Microsoft, Google, and Adobe all have resources detailing how to use their products, and Raspberry Pi and Micro:bit foundation, and many others have us covered with learning how to teach computing. But where are the resources that relate to the craft of teaching, the exciting and engaging stuff, the stuff that is a ‘bit out there? Where are the resources for teaching computing through film franchises, teaching computer science through Marvel films, or the Harry Potter computing activities?  Taking on a complicated concept, like chaos theory or machine learning, and making it accessible to younger students. Using retro games and computing, anyone doing anything with DOSbox, using old raspberry pi’s to make internet radios, using ham radio, Kodu, Minetest Magicavoxel? What about teaching computing through art or literature? I could go on, but this is the stuff that brought many of us to CAS in the first place.

I am inviting everyone to share their best ‘code:{ish}’ activity or resources. Something you have done in the classroom that was a joy to teach and tweaked your ‘nerd’ gene.

These activities are not necessarily linked to a curriculum or syllabus target. We can retrofit that later. They are not related to any issue of teaching programming or inspection. We do these activities because we enjoy them as much as the students. They primarily drive interest in the subject. As a result, I suspect these activities are going on by stealth. If we highlight them, we think somebody might stop us from delivering them because they are ‘not on the official curriculum.

You all have a ‘code:{ish}’ article in you. So if are interested in submitting a resource or blog. You can do the following:-

Get in touch with me at stuart.ball@bcs.uk with a few lines describing the outline of your idea.

Or

Upload your resource, you might like to write a short post and link to it.

Or

Write a blog post describing your activity/lesson.

Whatever you do, please use the following image as your header image. This will allow us to share the series better, bring selections together as a single resource and highlight the code:{ish} article of the month.

Download your image here
        """
    ),

    NewsItem(
        title="We are all teachers of technology…",
        url="https://www.computingatschool.org.uk/news-and-blogs/2022/october/we-are-all-teachers-of-technology",
        author="ALLEN Tsui | Primary School Teacher",
        date=datetime(2022, 10, 9),
        text="""The opening question of the Twitter: @TeacherTapp daily poll in early October 2022 about sharing resources got me thinking about why I freely share anything I've written or created in the line of duty in the way that I do.  Well, first and foremost it is principally because I firmly believe irrespective of which Key Stage, age range or school setting that any teacher works in, we are all teachers of technology.  We might not be explicitly be teaching all of the life-long skills as identified in the “Engineering Habits of Mind” developed by the Centre for Real World Learning at University of Winchester and the Royal Academy of Engineering (2014) but there will be some aspect of each of our teaching practices which touches on one, some or all of these attributes.

Professional Development delivered virtually

The @TeacherTapp poll question did make me realise too how as subject leaders in Primary schools, the arrangements to collaborate with colleagues will be dependent on subject as well as other factors.  Since I started working in schools in 2010 I have attended many training sessions which have focused on the core subjects.  I have no objection to this and wholly understand the necessity of doing so given the priorities of every Primary school.  It has however reminded me that given time constraints on all of us, by me freely sharing resources is a means of being able to provide a level of connection and support for colleagues who may or may not have the professional confidence to teach Computing.  It was presenting a workshop to ECTs which also made me realise that symbiotic benefit of sharing ideas with those who will never be expected to teach Computing given their own specialist roles since it sparks a fusion of new cross-curricular collaborative teaching and learning opportunities.

Beyond subject boundaries

In my mind therefore, I believe it is important as an active member of the Computing at School Community of Practice, that whatever our subject knowledge, practice and professional experiences, ‘we’ reach out and share more widely.  Social media has been instrumental in enabling the teaching community to do this.  It was indeed when I attended the Raspberry Pi Certified Educators workshop in May 2016 when Twitter: @LegoJames to be more active on social media and become a member of the Computing at School Community.

Computing at School

By virtue of the fact that you’re scrolling by this blog means that you are either already familiar with the Computing at School or maybe this is your first visit being newly appointed to the role of teaching Computing.  Some may be embarking on their teaching careers and heard their lecturers sign post membership or association with this incredible community.  Some may be industry experts who have only recently discovered this platform.  Irrespective of the path that brings you to this blog, welcome.

Since taking on the role of leading Computing at the amazing school I work for in Summer 2020, one of the frequently asked questions is ‘what’s the basis of your why?’  My own journey with the Computing at School started in 2016 where I met those involved with this grassroots organisation during the Raspberry Pi Certified Educators workshop that May in Newcastle. CAS as it is more familiarly known is supported by BCS, the Chartered Institute for IT.  CAS describes itself as a grassroots members based organisation or Community of Practice.  Formed by a body of volunteers in 2012, CAS has become a very influential network of Computing or Computer Science teachers as well as other associated experts from across the educational technology sector.  CAS is recognised by the UK Council of Subject Associations as one of three organisations representing Computing.  Notably, CAS is the only organisation of the three which does not charge a subscription for membership.

What has consistently impressed me since joining CAS has been how community spirited its members are with freely sharing ideas.  It has been though my associations with CAS that I have had the most amazing memory making moments for the children at the school I work for.  Whether it has been the opportunity to invite international delegations to my school, being a speaker on the main Arena stage opening the BETT Show, lifting the limits on learning about physical computing… 

@TsuiAllen on Twitter

Twitter is my preferred medium of social media since it allows me to exercise my stream of consciousness. I have actually had a Twitter account since August 2012 as Twitter @natachakennedy sign-posted me and my fellow students to during my PGCE year.  However, I had to have a ctrl-alt-del moment at the end of 2019.  Because I didn’t reboot my Twitter account until after the period for restoring my entire history of previous posts and contacts had expired, my account appears to have been only opened since the eve of the beginning of 2020.  It was during the time that the World went weird I decided to curate a social media persona focusing on the irreverent and frivolous rather than attempting to engage with controversial click-bait.

In the real World, I have been teaching at the school I work for since that Tim Peake began his mission aboard the International Space Station in December 2015.  However, where Tim Peake returned to Earth six months later, my mission at the amazing school that I work for continues.  I was a Class Teacher at the school until Summer 2020 when I was offered the opportunity to lead Computing.  With a three form entry, to provide non-contact, planning and preparation release time for the Classroom based colleagues, Computing is part of a provision lead by specialist teachers working across the whole school.  This means that I exclusively teach Computing to everybody from Reception to Year 6.  

For those who follow me on Twitter will know that I am an open source kind of individual as I freely share pretty much everything that I ever produce as part of my teaching practice.  In part it is to reciprocate the ethos of CAS sharing resources and ideas for free.  I have no ambition to build an entrepreneurial empire and commercialise or monetise the artefacts I produce.  The symbiotic professional gain I personally get from peer review feedback is worth more than any fiscal reward.  It is also in part my long succession strategy to provide immediate colleagues and the wider Computer Science teaching community resources that others can feel confident enough to use in their classrooms.  This is where social media and the CAS community has been a real asset enabling those schools with little or limited subject knowledge specialism to have access to a network of support and teach computing to the highest standards possible.

Sunday Scaries

Based on my own interactions of Twitter, one of the notable patterns is the peak in demand for sharing resources and teaching ideas on a Sunday.  This is often associated with what has become recognised by many as the ‘Sunday scaries’ or the sense of impending doom as the new working week looms.  I am happy to share my resources every #ShareStuffSunday hosted by Twitter’s @i_teach_things simply because social media provides me with what I consider a “safe space” to almost pre-published my resources before I put them into use.  What I mean is that if there is an audience of peers who are able to comment or feedback on what I share, it helps me focus on its subsequent use in the classroom.  I would much rather have my work openly critiqued by the wider teaching community since it also prepares me for similar conversations and meetings I expect from or with senior colleagues when they conduct their management scrutinies.  By sharing my resources openly to peer review means being able to evaluate my own practice as well as enabling my resources to be openly accessible for accounting and scrutiny purposes for when “An Inspector Calls…”

Simply selfish intention…

Whilst these ideas of professionally supporting others, peer review feedback as well as being openly accountable for scrutiny might be laudable to many, the underlying practical reason for sharing is just because I can.  Having subscribed to both Microsoft OneDrive and Google Drive since 2016 means being able to simply open the sharing link to any content I create and post the link as a message on Twitter, upload the file to the Computing at School website or since the end of 2020 posted as part of my @Wakelet collection.  Being a non-classroom based teacher means it is more practical to be able to openly access the files I want or need to use on a day to day basis without having to go through the increasingly complex and time consuming steps of password authentication.  By openly sharing my files too means establishing a virtual trail of what I have been working on so in the event I need to refer back to a file, I am able to always easily access a copy.

Some might suggest that such generosity is foolish given the quality of some of the resources I create or material I write might have some commercial value if I were to ever decide or choose to sell them.  Whilst I am pleased for those across the wider teaching community who extend their classroom expertise beyond their school and offer consultancy or provide their resources along a more mercantile model (whether by actual monetary exchange or ‘wish lists’ fulfilment), I simply personally prefer not to do that.   For me, commercialising what I create and write adds administrative complications, contradicting my underlying principle of wanting to improve the quality of teaching and learning Computing for everyone everywhere.

Thank you for reading.  """
    ),

    NewsItem(
        title="A simple demo of how pure functions simplify parallelisation",
        url="https://www.computingatschool.org.uk/news-and-blogs/2022/september/a-simple-demo-of-how-pure-functions-simplify-parallelisation",
        author="Richard Pawson",
        date=datetime(2022, 9, 28),
        text="""One thing that bugs me about teaching computer science is the amount of ‘rote learning’ – teaching pupils facts to memorise without understanding. 

As an example, one of the rote-learned facts about ‘functional programming’ (FP) – in the AQA A-level syllabus – is that writing systems from pure, side-effect free, functions makes parallelisation easier. But can a pupil at A-level standard really experience this for themselves? Here’s a nice example in C# with a VB translation at the end. (I’m afraid I don’t know Python in enough depth to know how to do it in Python, or even if it is possible – if anyone can help please do.)

Here's a functional approach to identifying all the primes up to a given value. It’s not an efficient efficient algorithm but it serves the challenge well, because it is computationally expensive:

static List<int> Primes(int upTo) => Enumerable.Range(2, upTo - 1).Where(n => IsPrime(n)).ToList();

static bool IsPrime(int n) => !Enumerable.Range(2, n / 2 - 1).Any(f => IsFactor(f, n));

static bool IsFactor(int f, int ofN) => ofN % f == 0;
We can time this (using the system stopwatch) generating all the primes up to 1 million:

using System.Diagnostics;
var sw = new Stopwatch();
sw.Start();
var result = Primes(1000000);
sw.Stop();
Console.WriteLine(sw.ElapsedMilliseconds/1000);
On my laptop (which has an Intel i7 processor) this task takes approx. 140 seconds. Because my Primes function is written using LINQ, which uses, and requires working with, side-effect free functions, I can easily parallelise this just by adding the call AsParallel() at the appropriate point, as shown here:

static List<int> Primes(int upTo) => Enumerable.Range(2, upTo + 1).AsParallel().Where(n => IsPrime(n)).ToList();
Running this again, took approx. 30 seconds on my laptop, which is a speed up of 3.8x. This is because my processor has 4 (physical) cores.

Observing the core usage

You can observe what is happening if you open the Resource Monitor (go to the Task Manager > Performance tab; there’s a link to the Resource Monitor at the bottom of the window).

Running the Primes function again, without the AsParallel(), I found that my processor was running at just under 30% capacity.  Surprisingly, perhaps, all the cores are being used, but – at least for the function execution itself (bear in mind there are other processes being run too) no more that one core is actually running the function at any given moment. (Why it is switching between cores is another discussion).

But running with the AsParallel() not only is the processor running at near 100% capacity overall but each of the cores is running at near 100%.

More detail

My processor actually has 8 ‘logical’ cores, but that is no advantage over the number of physical cores on a task like this, which is mathematically intensive, because each pair of logical cores has to share the arithmetic circuits. 

You are never going to get 4x improvement for two reasons:

The processor is still having to run other background processors for the operating system
There is some overhead from breaking up the data for parallelisation and then re-assembling it to generate the resulting list.
Translation into VB

Public Function Primes(upTo As Integer) As List(Of Integer)
    Return Enumerable.Range(2, upTo - 1).Where(Function(n) IsPrime(n)).ToList()
End Function
Public Function IsPrime(n As Integer) As Boolean
    Return Not Enumerable.Range(2, n / 2 - 1).Any(Function(f) IsFactor(f, n))
End Function

Public Function IsFactor(f As Integer, ofN As Integer)
    Return ofN Mod f = 0
End Function
And with the parallelism:

Public Function Primes(upTo As Integer) As List(Of Integer)
    Return Enumerable.Range(2, upTo + 1).AsParallel().Where(Function(n) IsPrime(n)).ToList()
End Function
        """)

]