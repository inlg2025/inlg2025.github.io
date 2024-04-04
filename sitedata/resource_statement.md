## Supplementary Materials Availability Statement Guide

**INLG 2024 Resources Track**

**Key Points**

- All papers accepted for publication at INLG 2024 must include a supplementary materials availability statement (even if only to state it can’t be made available or there aren’t any).
- If resources are made available, reviewers are requested to consult the resource as well as the paper.
- Papers should be self-contained.

Please find more details below.

**Usability and Reproducibility**

Usability of a resource or the data used or generated as part of the research as well as a clear understanding how it came about is a key component of progress in scientific research, to use such a resource competently in new research independently or to extend such a resource presented in scholarly publications or to reproduce the experiment. In the context of computer science, providing access to such material, such as code and datasets, greatly facilitates progress in research and reproducibility. This supports the independent verification of results, and can increase the impact of a work by allowing other researchers to reuse and build upon them. An important goal for INLG is to continue improving the reproducibility of all papers, and usability and reusability of the resources, where relevant.

**Supplementary material vs. Paper Content**

All papers submitted to INLG 2024 need to be self-contained, meaning that the body of the paper should provide a clear statement of their claims and clear argumentation regarding how these claims are substantiated by evidence. This includes any details that are important for interpreting the resource, such as the specifications of the machines used for experiments on the resource, key statistics about datasets, important configurations or hyper-parameter settings, details about the metrics used, details about how data was collected, etc.

The resource must include the materials reported in the paper that cannot feasibly be included in the paper itself.

We strongly encourage authors to make the resource available under open licenses and in repositories that provide long-term availability and have a persistent URI (Zenodo, Figshare, institutional repository, etc.).

**Purpose of the Materials Availability Statement**

While it has become increasingly common for papers to include links to supplemental material to help verify the results they present, often this is done in an ad hoc manner that differs from paper to paper.

To make it easier for readers to find the supplementary materials, to understand what is provided and what is not provided, and why, we ask all authors to include a standardized Supplementary Materials Availability Statement at the end of their paper that:

- lists all resources presented in the paper;
- points to locations where those resources can be found;
- if applicable, justifies why certain resources cannot be made available (e.g., the privacy, technical or legal concerns involved), or indicates the conditions under which they can be made available (if any).

**Format of the Supplementary Materials Availability Statement**

The Supplementary Materials Availability Statement should be placed at the end of the paper, just before the References (and before Acknowledgements, if present). It does not count in the 8 pages page limit. It should be formatted as an inline paragraph with an italicized heading:

---

_Supplementary Materials Availability Statement:_ Source code is available …

---

In Word, authors can simply replicate the formatting shown above.

In LaTeX, this can be achieved with the markup:

---

\paragraph\*{Supplementary Materials Availability Statement:} Source code is available …

---

**Content of the Resource Availability Statement**

The Statement should point to the location of all resources made available as presented in the paper. The authors must be careful to ensure that it is clear (either from the statement, or the resource linked from the statement) what versions, configurations, dependencies, steps, etc., are needed to use the resource. Some example templates of statements to include are:

- _Source code for our System X is available from …_
- _Datasets X, Y, Z are available from …_
- _Query sets X, Y, Z are available from …_
- _Source code for Baselines X, Y, Z is available from …_
- _The raw data used to generate Figure X, Y and Tables A, B are available from …_

Pointers to resources can be provided either directly in the text of the statement, as footnotes, or as bibliographical references; for example:

- _Source code for OurX is available from Github.<sup>1</sup>_
- _Source code for OurX is available from Github [1]._
- _Source code for OurX is available from Github at https://github.com/ThisIsUs/OurX._

If multiple resources are available at one location, statements can be combined, for example: “_Datasets A, B and query sets X, Y are available from …_”.

As per CfP, supplementary materials can be submitted via SoftConf.

In the unlikely case that the supplementary materials cannot be published openly, the authors must clarify this in the statement, summarizing why it cannot be published, and include details about the conditions under which the resource can be accessed; for example:

- _Source code for our System X cannot be made available due to plans to commercialize the software._
- _Dataset X cannot be made available as it incorporates private user data. However, a suitably anonymized version may be made available under a licence, upon contact with the authors._

**Examples of Supplementary Materials Availability Statements**

_Supplementary Materials Availability Statement:_ Source code for OurX and the queries used in Section 4 are available from Github.<sup>1</sup> The OurOntoX dataset is available from Zenodo [4]. The MyHealth dataset cannot be made available as it incorporates private user data.

---

1 https://github.com/ThisIsUs/OurX

References

…

[4] This, I.U. OurX. Zenodo doi:10.5281/zenodo.12345678. (2024) https://doi.org/10.5281/zenodo.4035223

…

**Review of the Supplementary Materials Availability Statement**

Reviewers will be asked to review the Availability Statement in order to verify that it does not omit any resources that are presented as novel resources in the paper, that the resources are indeed available at the locations indicated, and that all reasonable efforts have been made to make all relevant material available.

Reviewers are expected to review the content of the material. Nonetheless, it is important that the paper is self-contained, reporting on the resource and the context of its creation (refer to the full list of criteria in the CfP).
