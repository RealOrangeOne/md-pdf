<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:outline="http://wkhtmltopdf.org/outline"
  xmlns="http://www.w3.org/1999/xhtml">
  <xsl:template match="outline:outline">
    <html>
      <head>
        <link rel="stylesheet" href="{{ static_dir }}/style.css" />
      </head>
      <body class="tocs">
        <h1>Table of Contents</h1>
        <ul>
          <xsl:apply-templates select="outline:item/outline:item"/>
        </ul>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="outline:item">
    <li>
      <xsl:if test="@page!='2'">
        <div class="row">
          <a class="title">
            <xsl:if test="@link">
              <xsl:attribute name="href">
                <xsl:value-of select="@link"/>
              </xsl:attribute>
            </xsl:if>
            <xsl:if test="@backLink">
              <xsl:attribute name="name">
                <xsl:value-of select="@backLink"/>
              </xsl:attribute>
            </xsl:if>
            <xsl:value-of select="@title" /> 
          </a>
          <span class="page-number">
            <xsl:value-of select="@page" />
          </span>
        </div>
      </xsl:if>
      <ul>
        <xsl:apply-templates select="outline:item"/>
      </ul>
    </li>
  </xsl:template>
</xsl:stylesheet>
