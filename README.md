# Diptera genome analysis

I am intrigued by the investigation into the immunity of Flesh flies. As Diptera with an unclean lifestyle, one wonders how they manage to survive. This is indeed a fundamental question. I find their behaviour fascinating, as they are drawn to deceased animals, fecal matter, wounds of both animals and humans, putrid-smelling pitcher plants, and various forms of decaying material, including manure. They serve as major vectors for bacteria and even "viruses". Despite carrying such deadly organisms, they not only survive but also thrive in such environments.

What, then, is the secret to their immunity? The answers may lie hidden within their genomes. To gather information, I have embarked on data mining, utilizing publicly available dipteran genomes, as well as additional genomes obtained from the experts in the field. These genomes include those of Sarcophagidae, as well as other Diptera species that are equally, if not less, unclean. However, merely comparing genomes does not offer a conclusive answer to our question. Our hypothesis revolves around the possibility that a habitat rich in bacteria may drive the selection for increased diversity of immune components.

Insects possess a well-studied defensin gene that plays a crucial role in their immunity. By comparing this gene across the 59 different species of Diptera, including Sarcophagidae, we aim to generate informative results.

To accomplish this, I have opted to employ one of the popular linear models, namely the Hidden Markov model (HMM). I have developed a bioinformatics pipeline in Python that utilizes the defensin gene template and searches for matches within an extensive collection of genomes. Through this approach, the pipeline provides R values that aid in inferring the results and understanding the extent of genetic variation within Diptera species. Additionally, these results are used to generate phylogenetic trees, shedding light on the evolution of these genes.
## Results

![created first tree](https://github.com/prache/Digital-marketing-attribution/assets/25516674/37e38913-fa0a-471e-8163-86190d84591c)



![Screenshot from 2023-08-21 22-47-50](https://github.com/prache/Digital-marketing-attribution/assets/25516674/762e63ed-ee82-4fa0-bd78-d73969a07062)






