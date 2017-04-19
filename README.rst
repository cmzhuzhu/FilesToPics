|

NAME
====

    FileToPics

|

Environment
===========

	Java：

    yum -y localinstall jdk-8u101-linux-x64.rpm


    LibreOffice：

    tar zxf LibreOffice_5.2.2_Linux_x86-64_rpm.tar.gz
    cd LibreOffice_5.2.2.2_Linux_x86-64_rpm/RPMS/
    yum -y localinstall *.rpm

    tar zxf LibreOffice_5.2.2_Linux_x86-64_rpm_langpack_zh-CN.tar.gz
    cd LibreOffice_5.2.2.2_Linux_x86-64_rpm_langpack_zh-CN/RPMS
    yum -y localinstall *.rpm


    Fonts：

    yum groupinstall "fonts"


    ImageMagick：

    yum -y localinstall ImageMagick-libs-7.0.3-4.x86_64.rpm
    yum -y localinstall ImageMagick-7.0.3-4.x86_64.rpm
    yum -y localinstall ImageMagick-devel-7.0.3-4.x86_64.rpm

|

Use
===
    pip install FileToPics

|

SYNOPSIS
========

.. code-block::


    from FileToPics import FileToPics

    file2pics = FileToPics(filePath = '/home/test.pdf', picPath = '/home/', fileType = 'pdf')
    res = file2pics.fileToPicture()

    file2pics = FileToPics(filePath = '/home/test.pptx', picPath = '/home/', fileType = 'ppt')
    res = file2pics.fileToPicture()


|

DESCRIPTION
===========
    This Python package can turn file(ppt/pptx/doc/docx/wps/pdf..) into pictures

    Params:

    filepath : you want to operate the source file path
    picpath  : Image storage path(In / at the end)
    filetype : operate the source file type
    pictype  : You want to generate the image format(default webp)

    Notice:
    params filepath and filetype does not match will be reported to the wrong