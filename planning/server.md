# Server
## Overview
Of course, the clients will run on several devices, at the beginning only machines that
are able to run a ``.exe`` file. Perhaps there will be a mobile version of the client too
but that should not be part of this section. Within this Markdown file, I wanted to explain
where the server instance will handle its tasks for my case. That means, that the server
can be setup on every machine that is able to work with Python and has enough resources to
run the server program. I am only talking about my specific case and how I am planning to 
create everything needed, so i have something like a little documentation for myself and
people I will explain the whole project in the near future.

## Hardware
I decided to use a **Raspberry Pi 3B** for the server, it has more than enough resources to
handle all incoming RPCs, is more energy efficient than most other solutions and is
uncomplicated to setup when it comes to operating systems and the software dependencies.

## Software
One reason why I chose Python for the server program and not C# or other languages, is
following one: Since I already knew very early that I will use a Raspberry, I could not use
some "heavier" languages like C# for example. Python is easy to install and ``.py`` files
can easily be ran on a **Linux distribution**. Talking about the operating system, you may
also wonder which Linux distribution I will use. Because I already worked a few times with a 
Raspberry Pi and Python, I have already gained some experiences with **Ubuntu Server**. That
is why I continue using it. But there are also some more tools in use for this whole project.
Besides **gRPC** in combination with **WPF/C#** and **Python**, I want to create a database
containing all users that communicate via "UnChat". You might already know my login/register
window and so on. All of this needs a database to get the data from and for this, I will use
a simple **MySQL database** on my server. It is also possible that all sent message will be
encrypted in the future but first of all I have to work on the server and connection to all
clients.