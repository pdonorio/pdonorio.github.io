
# The latest news from the developer meeting

Hi there, I'm back from our latest face-to-face meeting for `EUDAT`.

There are some new interesting changes for the `HTTP-API` of the `B2STAGE` service so I thought I'd write down a few things and share to users to give updates on what's happening.

## The most important milestone

First of all we can now share a great announcement:
The HTTP-API stable version [has just been released]().

We reached the most important milestone we had, so finally `1.0.0` is out!

We took the chance of the past meeting to present the current results and to refine some final decisions; now we feel we are ready to go to production and I'm glad we made it so far.

## What's next

Now that the code is stable we are planning how to roll over the existing EUDAT `B2SAFE` instances across Europe data centres.

I will be coordinating with our administrators at [`CINECA`](http://www.hpc.cineca.it/) to be one of the first to provide access to EUDAT users to this new interface onto their datasets we have.

## How to update your existing installation

If you already tested locally an alpha, beta or release candidates the best option is not to upgrade. Please choose to clean up all your containers, images and relative volumes so far, instead.

We rolled an `upgrade` feature in the underlying `rapydo` framework, but it seems not capable of working with older versions. But if backup your configuration files that were eventually changed, any other data file and clone again the release within another directory, nothing else will be needed as your data is preserved at the `B2SAFE` level.

## B2ACCESS authentication

We also expect to release a patch as soon as possible, right after receiving new feedback from deploy and usage of the project in production.

We will make treasure of that time since we also are currently debugging through the HTTP-API the current issue of trusting certificates between `B2ACCESS` and `B2SAFE`. We've setup a new coordination through teams to dig down the `openssl` and `GSI` problems that are currently behind the setup.

We expect to re-enable the authentication endpoint towards the `B2ACCESS` service by the time the first patch is out.

