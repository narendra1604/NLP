<VirtualHost *:80>

  # REQUIRED. Set this to the host/domain/subdomain that
  # you want this VirtualHost record to handle.

  ServerName ssltest.atiqur.xyz

  # Optional. You can specify additional host names that
  # serve up the same site. This can be top-level, domains,
  # sub-domains, and can even use wildcard subdomains such
  # as *.yourdomain.com - just separate each host name
  # with a single space.

  ServerAlias www.awswithatiq.com

  # REQUIRED. Set this to the directory you want to use for
  # this vhost site's files.

  DocumentRoot /var/www/html/aws

  # Optional. Uncomment this and set it to your admin email
  # address, if you have one. If there is a server error,
  # this is the address that Apache will show to users.

  ServerAdmin info@awswithatiq.com

  # Optional. Uncomment this if you want to specify
  # a different error log file than the default. You will
  # need to create the error file first.

  #ErrorLog /var/www/vhosts/logs/error_log

  # REQUIRED. Let's make sure that .htaccess files work on 
  # this site. Don't forget to change the file path to
  # match your DocumentRoot setting above.
  
  <Directory /var/www/aws>
    AllowOverride All
  </Directory>

</VirtualHost>