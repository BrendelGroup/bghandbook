# Literate programming

There are several critical components of any computational science project.
- **inputs**, usually in the form of one or more data files
- **outputs**; could be processed data, summary statistics, or data visualizations
- **methodology**, usually in the form of code; in other words, how precisely do you go from input to output?
- **documentation**, usually in the form of written prose; discuss motivation and hypotheses, defend parameter choices, provide interpretation, and so on

Communicating all of these project components to fellow colleagues can be a considerable organizational challenge.
Input and/or output files may be large in size or number.
Prose is in a text/Markdown file, code is in another file, and graphics are in yet another file.
How do you effectively organize and communicate all of these pieces?

A couple of fairly new tools based loosely on the concept of *literate programming* provide one solution to this challenge.
The idea is to create a dynamic document with code and corresponding output interjected into a narrative flow.
Within the document code can be written, executed, and re-written, and the environment automatically captures the textual and/or graphical outputs of the code for presentation in real time.
The result is a document that is fully reproducible, providing  (ideally) a complete representation of all critical project components as discussed above in an easy-to-share and easy-to-edit package.

Two tools, [RStudio](http://rmarkdown.rstudio.com/) and [Jupyter Notebook](http://jupyter.org/index.html), have become very popular tools for creating such dynamic documents.
A brief overview of these tools is provided below.

## RStudio

RStudio is a data analysis environment for the statistical programming language R.
In RStudio, you can create an *R Markdown* document containing prose text formatted in Markdown, interspersed with chunks of R code.
With the click of a button, RStudio will convert the Markdown to HTML, execute the R code, and paste any output or graphics produced by the code into the HTML file (alternatively, RStudio can produce PDF output).

## Jupyter Notebook

Jupyter Notebook is a browser-based tool for creating dynamic documents.
It is implemented in Python, and Python is the default language for code, but there is support for dozens of other languages, including R, Bash, Perl, JavaScript, and more.
A Jupyter notebook consists of a sequence of "blocks", each block either containing Markdown-formatted text or code and and corresponding output.
Each block can be rendered or executed independently, or the entire document can be rendered/executed in one fell swoop.

## Comparison

Fundamentally, these tools are very similar.
They both support mixing prose (formatted in Markdown) with code and the output of that code.
There are a few significant differences though.
- Jupyter offers the option of piecewise rendering and execution, whereas RStudio supports only rendering of complete Markdown documents.
  This can be a blessing and a curse: piecewise execution enables rapid testing of different settings or parameters, which could potentially take much longer if the entire notebook is large and requires tens of seconds to render.
  However, piecewise execution introduces the risk of a code block coming out of sync with its corresponding output or with other code blocks.
  Before saving a Jupyter notebook, it is wise to "reset the kernel" (flush all variables and start with a clean slate) and execute all blocks one more time to make sure that piecewise rendering has not broken the flow of the code.
- Jupyter offers support for many languages, whereas RStudio supports only code in R.
- Jupyter notebooks (encoded as JSON files) are rendered automatically by GitHub, whereas R Markdown files must be manually rendered to HTML or PDF before they are shared.
