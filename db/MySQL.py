# install 
# sudo apt update
#sudo apt install mysql-server
# sudo mysql_secure_installation

# setting
# sudo mysql_secure_installation

# authentication (add password)
# sudo mysql
# mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
# mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new password';

# applying changes:
# mysql> FLUSH PRIVILEGES; 

# mysql> exit

# db entry
# mysql -u root -p

# show databases; 

# create database test


