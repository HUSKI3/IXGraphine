
echo "Installing IXGraphine"
#cd dev 
#pip3 install -r requirements.txt &&
#npm install . 
sudo mkdir /etc/IXGraphite
sudo cp -Pr dev /etc/IXGraphite
echo "Creating shortcut"
sudo chmod u+x /etc/IXGraphite/IXGrapite.desktop
sudo cp -Pr dev/IXGraphite.desktop ~/Desktop
