libaacplus
==========

AAC+ (HE-AAC) v2 built into an RPM for el6.

This is an unofficial package for 64-bit RHEL/CentOS 6 (el6) so I don't have to build from source every time.

Purpose, Limitations
--------------------

This was built specifically for Darkice 1.2. Darkice looks in /usr/lib (it does not check lib64 even if on an x86_64 system) so this package drops the libs in /usr/lib. Any utilities which expect libaacplus.so to be in /usr/lib64 will be sorely disappointed. This can be remedied in one of two ways.

The simple way to fix this is to symlink all the libaac things like so

```
ln -s /usr/lib/libaac* /usr/lib64/
```

The second way is to change a few things in the .spec file and run ```rpmbuild -bb libaacplus.spec```. I won't explain the changes needed because if you aren't able to do it on your own you will run into more trouble than it is worth. Honestly, the symlink method is easiest :)

Compatibility
-------------

Built and tested on RHEL 6.5, should be compatible with all RHEL 6 and equivalent.


Installation
------------

Download the package then install using ```yum``` not ```rpm```. This ensures RPMDB isn't altered outside of yum and is the recommended way of installing rpms.

```
yum install libaacplus-2.0.2-1.el6.x86_64.rpm
```


History
-------

This is current (2.0.2) as of this writing (May 2014).

The source was probably last updated sometime in 2010. The project seems to be on hiatus.


Original
--------

Project page: http://tipok.org.ua/node/17
