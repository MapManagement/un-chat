# Cancellation and Shutdown
## Overview
It already works that one login from a client only needs one channel which should be closed after the specific
user logged out. In theory it does but the praxis is a bit different, more about it in my client repository. 
Nonetheless, if I want to finish or cancel all running RPC streams, I cannot just shutdown the whole channel, 
no, I have to cancel all running streams manually and in my case the client has to do that once he/she closed
the application or simply just logged out the user account. There are dozens of possibilities how to do
something like that, depending on your language, the proto services and the way your application works. That
is the main reason why I probably put that much time into this topic, more than in any other problem I
experienced so far.

## Workflow
I think it is better to create a scheme how I want my application to interact with the server when it comes
to opening and closing channels/calls. Since I am using a Raspberry Pi, I really have to care about my
resources and therefore a good concept of closing unnecessary channels and streams:
1. user starts client application and logs him-/herself in
2. user does what a user does: sending, reading messages and so on -> RPC stream is started
3. until the user logs out, the server does not close any needed stream or channel
4. user closes application or logs out -> no interaction with server anymore
5. client has to provide the information that user logged out (``CancellationToken``), tries to shutdown the
opened channel (``ShutdownAsync``)
6. server should now close all corresponding streams and the corresponding channel  
**eventually frees resources**

## Problem
I found a way, although it is probably not recommended to do so, to "access" a cancellation while the
message stream runs. I simply just send a message with a specific ``senderID`` and ``recipientID``. Of course,
no other user has or can get his ID. The server is now able to check every incoming request on the basis of
those IDs and once the set "cancellation ID" comes in, the server can close/cancel the stream. If it was that
easy, I already would be working on other things but unfortunately I am not. On one hand, I always cancel
not only the connection to the logged out client, no, I will destroy the whole message stream. Every
connected client will not receive new responses as soon as one client logged out, since I either ``return``
the function or I ``context.cancel()`` all streams (found a fix while writing this :D). On the other hand,
the thread is still running after I did one of the previously explained methods, even though the thread only
starts running whenever I open a new message stream. The possibilities are, that I still do not close the
stream properly or there is another thread that has to be finished which I do not know yet. More tests and
researches will hopefully bring light into the darkness.