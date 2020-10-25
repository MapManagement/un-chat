# Main idea of "Un Chat"
Simple chat platform which lets users communicate via a GUI. Users should be able to communicate just
by adding another user(s) (how is not defined yet) and writing them by using the GUI and the given
control elements found within it. All messages are handled by a program running on a dedicated
server which then redirects the data to the targeted user. That receives the message and will be able
to send messages back. Especially the technical parts of the project are described in the following
chapters.

# Server Side
## ❗ Necessary
- handling all incoming requests
- forwarding all messages to the targeted user
- handling multiple chats (not only two users will try to communicate)
- server to run the program on
- saving user profiles
## ❓ Possible
- encryption for sent messages
## ⚙️ Technologies / Frameworks / Languages
- [Python](https://www.python.org/)
- [gRPC](ttps://grpc.io/)

# Client Side
## ❗ Necessary
- creating a GUI for desktops
- opening different chats and adding other users
- sending messages to other users
- receiving message from other users
- creating a profile
## ❓ Possible
- also sending other file formats e.g. pictures or videos
- mobile support
- reporting users
## ⚙️ Technologies / Frameworks / Languages
- [C#](https://docs.microsoft.com/en-us/dotnet/csharp/)
- [WPF](https://docs.microsoft.com/en-us/dotnet/desktop/wpf/?view=netdesktop-5.0) for desktop application
- [Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor) or [Xamarin](https://dotnet.microsoft.com/apps/xamarin) for mobile application
