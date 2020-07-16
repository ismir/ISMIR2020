---
layout: page
title: Tutorials
permalink: /tutorials/
---

# Session A

## Tutorial A1

<div class="tutorial-subtitle">
  <div>Analysis of Expressive Timing in Recorded Music Performances</div>
  <div>Nico Schüler</div>
</div>

#### _Abstract_

This tutorial will briefly summarize research on expressive timing in music, present an original research project (as an example) on rubato in four performances of Bach’s Invention No. 9, explain and demonstrate how to use the freeware Sonic Visualiser as well as Excel for the analysis of expressive timing in music, and participants will, with the help of the tutorial leader, pursue their own analysis of other performances of Bach’s Invention No. 9. (Recordings will be provided.) We will combine the data collected (in Excel files) to look for similarities and differences in the various performances and how expressive timing correlates to certain musical features. (An analytical score of the piece will be provided.) We will collectively formulate research findings.

This tutorial is suitable for anyone who is curious about the topic. Beyond curiosity, participants do not need to have a music or computer science background. Those interested in participating in the analyses should bring a laptop (Windows computer or Mac) to the tutorial, with Sonic Visualiser (<http://sonicvisualiser.org>) and the VAMP plugin “Note Onset Detector” (<http://www.vamp-plugins.org>) installed.

#### _Presenter_

Professor Dr. **Nico Schüler** (b. 1970), is University Distinguished Professor of Music Theory & Musicology at Texas State University. His main research interests are computer applications in music research, methods and methodology of music research, interdisciplinary aspects of 19th/20th century music, music theory pedagogy, and music historiography. He has given numerous international workshops on computer-applications in music. He is the editor of the research book series Methodology of Music Research, the author and / or editor of 21 books, and the author of more than 120 articles. Among his most recent books are Musical Listening Habits of College Students (2010) and Computer-Assisted Music Analysis (2014). <http://www.nicoschuler.com>, <nico.schuler@txstate.edu>.

## Tutorial A2

<div class="tutorial-subtitle">
  <div>Metric Learning for Music Information Retrieval</div>
  <div>Brian McFee, Jongpil Lee, Juhan Nam</div>
</div>

#### _Abstract_

Metric learning is a paradigm of representation learning, in which proximity between the representations of items is optimized to correspond to a notion of similarity. Compared to the classification, metric learning can leverage more flexible forms of supervision, for example, two audio clips belong to the same artist or not, or have the same tempo or not. This enables the learning model to take a large or indefinite number of classes. Moreover, metric learning handles the embedding space directly by measuring the distance between the transformations of different examples. This facilitates usage of different domains or modalities of inputs in the same framework (e.g., audio embedding in one input and word embedding in another input). Such flexible and adaptable characteristics of metric learning have been enjoyed in many of machine learning tasks, particularly, similarity-based content retrieval. In recent years, interest in metric learning from the MIR community has also increased. Considering the multi-faceted and hierarchical-level of notions in similarity (e.g., semantic-level, score-level or audio-level) and diverse forms of data (e.g., audio, MIDI, text labels, lyrics, album covers, and user data), we see a great potential of metric learning in music. Therefore, introducing the method in an educational manner and surveying recent progress will be timely and helpful to relevant researchers. In this tutorial, we plan to present three lectures as follows:

1. **Metric learning foundations**: This lecture introduces mathematical foundations of metric learning.
2. **Deep metric learning and applications to MIR (1): core tasks** - This lecture introduces recent deep metric learning methods and their applications to music classification and similarity-based retrieval tasks.
3. **Deep metric learning and applications to MIR (2): variations** - This lecture introduces various applications of deep metric learning in MIR, showing how researchers have bridged diverse domains and modalities of input in metric learning.

#### _Presenters_

**Brian McFee** is Assistant Professor of Music Technology and Data Science New York University. He received the B.S. degree (2003) in Computer Science from the University of California, Santa Cruz, and M.S. (2008) and Ph.D. (2012) degrees in Computer Science and Engineering from the University of California, San Diego. His work lies at the intersection of machine learning and audio analysis. He is an active open source software developer, and the principal maintainer of the librosa package for audio analysis.

**Jongpil Lee** received the B.S. degree in electrical engineering from Hanyang University, Seoul, South Korea, in 2015, the M.S. degree, in 2017, from the Graduate School of Culture Technology, Korea Advanced Institute of Science and Technology, Daejeon, South Korea, where he is currently working toward the Ph.D. degree. He interned at Naver Clova Artificial Intelligence Research in the summer of 2017 and at Adobe Audio Research Group in the summer of 2019. His current research interests include machine learning and signal processing applied to audio and music applications.

**Juhan Nam** is an Associate Professor of the Graduate School of Culture Technology at the Korea Advanced Institute of Science and Technology (KAIST), South Korea. Before joining KAIST, he was a staff research engineer at Qualcomm. Before his research career, he was a software/DSP engineer at Young Chang (Kurzweil). He received the Ph.D. degree (2013) in Music from Stanford University, studying at the Center for Computer Research in Music and Acoustics (CCRMA). He is interested in various research topics at the intersection of music, signal processing, and machine learning.

## Tutorial A3

<div class="tutorial-subtitle">
  <div>Prototyping and Scaling Audio Research with Klio</div>
  <div>Fallon Chen and Lynn Root</div>
</div>

#### _Abstract_

This tutorial will walk attendees through the use of a Python framework called klio that makes use of the Apache Beam Python SDK to parallelize the execution of audio processing algorithms over a large dataset. Apache Beam is a portable and extensible programming model that unifies distributed batch and streaming processing. It manages the I/O and parallelized execution needed for large-scale data processing. Any audio processing algorithm that can be executed by a Python process and has dependencies that can be installed on machines supported by Apache Beam runners can be run with klio. Audio processing algorithms that have been added to a klio data processing job can be run locally on the practitioner's machine, before being run on large-scale data processing systems like Google Cloud Dataflow. This enables the practitioner to make quick local changes to their algorithm and test it on a few files before deploying a longer running job on more files.

The intended audience of this tutorial are audio processing practitioners who have wrestled with the complexity of iterating upon and coordinating the execution of algorithms that both consume and produce large audio datasets. klio provides best-practice standards and abstractions, encoded in its Python-based command line interface and API, that help audio practitioners prototype, organize and scale their work.

During the tutorial, attendees will receive:

* An overview of klio that establishes core concepts and features
* Guidance through building a klio audio processing graph and running it on an audio dataset

#### _Presenters_

**Fallon Chen** is a Senior Engineer at Spotify, where she builds libraries and tools for audio processing. She holds a M.S. in Computer Science from the University of California, San Diego, and a B.S. in Computer Science from the University of California, Davis. Her favorite genre is industrial techno.

**Lynn Root** is a Staff Engineer at Spotify and resident FOSS evangelist. She is a seasoned speaker on building and maintaining distributed systems, and maintains Spotify's audio processing framework. Lynn is a global leader of diversity in the Python community, and the former Vice Chair of the Python Software Foundation Board of Directors. When her hands are not on a keyboard, they are usually holding a bass guitar.

# Session B

<!-- ## Tutorial B1

<div class="tutorial-subtitle">
  <div>Sound Morphing: At the Crossroads of Perception and Creativity in MIR</div>
  <div>Marcelo Caetano and Charalampos Saitis</div>
</div> -->

## Tutorial B1

<div class="tutorial-subtitle">
  <div>Version Identification in the 20s</div>
  <div>Furkan Yesiler, Christopher Tralie, Joan Serrà</div>
</div>

#### _Abstract_

The version identification (VI) task concerns detecting and retrieving a set of songs that originate from the same underlying musical composition. Versions (or cover songs) convey the same musical entity while incorporating differences in several musical characteristics, including the differences in timbre, tempo, key, lyrics, and even added/deleted sections. The main applications include digital rights management and music catalog organization.

For more than a decade, VI systems suffered from the accuracy-scalability trade-off, with attempts to increase accuracy resulting in cumbersome, non-scalable systems. Recent years however have witnessed an increase in deep learning-based VI approaches that take a step toward bridging the accuracy-scalability gap, and we start seeing the possibility to deploy such systems in real-world applications. Although this trend positively influences the number of researchers and institutions working on VI, it may also result in obscuring the literature before the deep learning era. To appreciate the 20 years of novel ideas in VI and to facilitate building better systems in the next decade, we believe that now may be the right time to review some of the successful ideas and applications proposed in VI literature and connect them to current systems and ideas.

We will start the tutorial by explaining common input representations and feature post-processing steps. We will continue with comparing the pros and cons of alignment-based and embedding-based approaches, which constitute the two main perspectives for similarity estimation in VI. Lastly, after discussing a number of ideas that can be incorporated into any VI system, we will conclude by presenting the current challenges and future directions in VI research. Our goal is for the audience to leave with a thorough appreciation of both the history of the task and current directions, and that this context will allow them to jump into conducting novel research in the area.

#### _Presenters_

**Furkan Yesiler** is a PhD candidate at the Music Technology Group (MTG) of Universitat Pompeu Fabra (Barcelona). His research is focused on leveraging deep learning techniques to build accurate and scalable music version identification (VI) systems for industrial use cases. His recent contributions include MOVE, a state-of-the-art VI system based on musically motivated principles; Da-TACOS, a large-scale VI benchmark set; and acoss, an open-source framework for feature extraction and benchmarking designed for VI. He received his MSc in Sound and Music Computing also from the MTG, with a focus on singing voice research. He graduated summa cum laude with two BSc degrees in computer engineering and industrial engineering from Koc University (Istanbul), where he was accepted with a full scholarship. During his bachelor’s studies, he did internships in management consulting and M&A advisory companies in Istanbul, managed a student club with 200+ members, participated in a number of rowing competitions and musical theater shows, and spent a trimester at the University of California, Santa Barbara.

**Christopher Tralie** is an assistant professor in Math and Computer Science at Ursinus College in Collegeville, Pennsylvania, USA. He works in applied geometry/topology and geometric signal processing, and his work spans shape-based music structure analysis and version identification, video analysis, multimodal time series analysis, and geometry-aided data visualization. He received a B.S.E. from Princeton University 2011, a master’s at Duke University in 2013, and a Ph.D. at Duke University in 2017, all in Electrical Engineering. His Ph.D. was primarily supported by an NSF Graduate Fellowship, and his dissertation is entitled “Geometric Multimedia Time Series.” He did a postdoc at Duke University in Mathematics and a postdoc at Johns Hopkins University in Complex Systems. He was awarded a Bass Instructional Teaching fellowship at Duke University, and he maintains an active interest in pedagogy and outreach, including longitudinal mentoring of underprivileged youths in STEAM (STEM + arts) education.

**Joan Serrà** is a staff researcher with Dolby Labs in Barcelona since 2019, where he works on deep learning and audio processing. He did his MSc (2007) and PhD (2011) in automatic version identification at the Music Technology Group of Universitat Pompeu Fabra. He also did a postdoc in artificial intelligence at IIIA-CSIC (2011–2015). After that, he was a machine learning researcher at Telefónica R&D (2015–2019). He has had research stays at the Max Planck Institute for the Physics of Complex Systems (2010) and the Max Planck Institute for Computer Science (2011). He has been involved in more than 10 research projects, funded by National and European institutions, and co-authored over 100 publications, many of them highly cited and in top-tier venues, including NeurIPS, ICLR, ICML, InterSpeech, ICASSP, and ISMIR.

## Tutorial B2

<div class="tutorial-subtitle">
  <div>Open-Source Tools & Data for Music Source Separation: A Practical Guide for the MIR Practitioner</div>
  <div>Ethan Manilow, Prem Seetharaman, Justin Salamon</div>
</div>

#### _Abstract_

Musical source separation has become increasingly effective in recent years. As such, applications of music source separation have the potential to touch many aspects of MIR research. However, from a user’s perspective, either in doing source separation research from scratch or in applying source separation to other tasks (e.g. polyphonic music transcription), there are still significant roadblocks. Code and data are released on a paper-by-paper basis, making it difficult to compare, use and extend existing techniques. This limits the usefulness of source separation for researchers not actively steeped in its many nuances, and hinders its applicability to broader MIR research.

In this tutorial, we present a set of complementary, easy-to-use, open-source tools and datasets for source separation research, evaluation, and deployment. We show how they interlock with one another, and how they can be used in concert to structure source separation within a project for research or deployment. Finally, we propose a generic and well-tested project structure for efficiently doing modern source separation research, from sweeping over hyperparameters, to setting up competitive baselines, to augmenting your datasets.

Participants of this tutorial will leave with:

1. A practical overview of source separation including history and current research trends.
2. The ability to make educated decisions about how to best include source separation in their workflow.
3. The ability to select the proper separation algorithm or a pre-trained model for their research.
4. The ability to effectively train a custom model for their research using open-source tools.

Our tutorial is aimed at researchers and practitioners that are familiar with audio and machine learning but have little or no experience with source separation. Our primary resources will be the following open-source/data projects: [nussl](https://github.com/nussl/nussl), [scaper](https://github.com/justinsalamon/scaper), [Slakh2100](http://www.slakh.com/), and [MUSDB18](https://sigsep.github.io/datasets/musdb.html). References to additional tools and datasets (including for non-music audio) will be provided.

#### _Presenters_

**Ethan Manilow** is a PhD candidate in Computer Science at Northwestern University under advisor Prof. Bryan Pardo. His research lies in the intersection of signal processing and machine learning, with a focus on source separation, automatic music transcription, and open source datasets and applications. Previously he was an intern at Mitsubishi Electric Research Labs (MERL) and at Google Magenta. He is one of the lead developers of nussl, an open source audio separation library.

**Prem Seetharaman** is a research scientist at Descript in San Francisco. Previously, he was a teaching fellow at Northwestern University, where he received his PhD in 2019 advised by Bryan Pardo. The objective of his research is to create machines that can understand the auditory world. He works in computer audition, machine learning, and human computer interaction. He is one of the lead developers of nussl, an open source audio separation library, and Scaper, a library for soundscape generation & augmentation.

**Justin Salamon** is a research scientist and member of the Audio Research Group at Adobe Research in San Francisco. Previously he was a senior research scientist at the Music and Audio Research Laboratory and Center for Urban Science and Progress of New York University. His research focuses on the application of machine learning and signal processing to audio & video, with applications in machine listening, representation learning & self-supervision, music information retrieval, bioacoustics, environmental sound analysis and open-source software & data. He is the lead developer of Scaper, a library for soundscape generation & augmentation.
