

sudo apt update    # Fetches the list of available updates
sudo apt upgrade   # Installs some updates; does not remove packages
sudo apt dist-upgrade  # Installs updates with smart handling of dependencies, and removes obsolete packages


sudo fallocate -l 4G /swapfile  # Allocates a 4GB file to use as swap
sudo chmod 600 /swapfile       # Sets the correct permissions for the swap file
sudo mkswap /swapfile          # Marks the file as a swap space
sudo swapon /swapfile          # Enables the swap space
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab  # Makes the swap space permanent