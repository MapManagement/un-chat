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