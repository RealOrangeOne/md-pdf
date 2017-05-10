# Markdown

Whilst `md-pdf` theoretically supports all formats pandoc does, it's only been tested and and validated to support markdown.
 
Information about markdown as a format can be found [here](http://daringfireball.net/projects/markdown/). The standard format and syntax is used, however there are some additional features to improve the output format.

### Images
Images take the same syntax as with standard markdown: 
   
    ![title](url)

Referencing files inside your project directory can be done with a path relative to the project directory. You can use images direct from online, however you'll need to be connected to the internet when generating.

The title for the image is also used as the caption, and is displayed directly under the images.


### Linking
You can link to other parts of your document by their titles, in the same way linking to ids works on the web.


For example, if you had a title _Some Title_, then you can link to it like:

    [Click Here!](#some-title)

__Note__: The header size doesnt matter. You link to an h4 tag the same as linking to an h1.
