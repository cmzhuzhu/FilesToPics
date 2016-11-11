Name

    FileToPics

Environment：

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
    
Use
 
    pip install FileToPics


SYNOPSIS

    from FileToPics import FileToPics

    file2pics = FileToPics(filepath = '/home/test.pdf', picpath = '/home/', filetype = 'pdf')
    res = file2pics.file_to_pics()

    file2pics = FileToPics(filepath = '/home/test.pptx', picpath = '/home/', filetype = 'ppt')
    res = file2pics.file_to_pics()


DESCRIPTION

    This Python package can turn file(ppt/pptx/doc/pdf..) into pictures
    
    Params:

    filepath : you want to operate the source file path
    picpath  : Image storage path(In / at the end)
    filetype : operate the source file type
    pictype  : You want to generate the image format(default webp)

    Notice:
    params filepath and filetype does not match will be reported to the wrong

