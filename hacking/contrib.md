# Contributing

## General
* Join the [Discord channel](https://discord.gg/P7FYThy)
* Join the [mailing list](http://sourceforge.net/p/blackmagicdebug/mailman/)
* Edit this wiki
* Use [Linux kernel coding style](https://www.kernel.org/doc/html/latest/process/coding-style.html)
* Submit changes with [Github pull-requests](https://guides.github.com/introduction/flow/)

## Patch Policy (draft)
 - [@esden](https://github.com/esden) is the maintainer of the project.
 - [@dragonmux](https://github.com/dragonmux) is deputy maintainer answering to [@esden](https://github.com/esden)
 - If you have any questions regarding the contribution process either contact [@esden](https://github.com/esden) or [@dragonmux](https://github.com/dragonmux)
 - Every Pull Request has to build and pass all tests on top of the `main` branch before it can be merged.
 - Every Pull Request requires review from one of the maintainers.
 - Because we can't test all possible hardware platforms, we will need target specific maintainers to test and approve non-trivial changes to target support code.
 - Trivial patches such as adding a device ID to a switch statement may be merged without approval.
 - We generally follow the "optimistic merge policy". This means that unless there are significant issues with the patch we will try to merge all patches assuming they are 100% correct, and we will not try to be nitpicky about every detail. That said, please use the review comments from the maintainers as guidance for future contributions to save maintainer time down the road. Repetitive contributions of low quality code will result in your Pull Requests being ignored and closed without being merged. So please do your best to improve your contribution quality to match our standards.
 - All existing code may be assumed to be maintained by @esden, as patches appear that we can't test we will ask for a volunteer maintainer on Discord or approach someone directly based on git history of the code in question.
 - Patches for new targets that don't affect existing targets will be merged
without further testing assuming they conform to style and don't do anything stupid.  The author becomes the maintainer for that target.
 - If the code is orphaned and no maintainer can be found in reasonable time, the patch author may take over as the new maintainer.
 - The current maintainer should be noted in the copyright banner at the top of the file in question.
 - The Github request review feature of pull requests should be used to request a review from the maintainer.

