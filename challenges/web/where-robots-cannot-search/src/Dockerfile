# Dockerfile for web - Where robots cannot search
FROM httpd:2.4-alpine

RUN sed -i 's|#LoadModule rewrite_module modules/mod_rewrite.so|LoadModule rewrite_module modules/mod_rewrite.so|' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's|AllowOverride None|AllowOverride All|' /usr/local/apache2/conf/httpd.conf

COPY ./html/ /usr/local/apache2/htdocs/
