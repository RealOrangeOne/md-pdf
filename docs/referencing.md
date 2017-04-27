# Referencing

Referencing is powered by `pandoc-citeproc`, so any format supported by it is supported. A list of supported formats can be found [here](https://github.com/jgm/pandoc-citeproc/blob/master/man/pandoc-citeproc.1.md).

__Remember__: To use YAML, your file must end `.yaml` rather than `.yml`!

## CSL Files
There are many different ways of referencing, both inline, and in a bibliography. `md-pdf` supports _all_ of them.

The configuration used for this is stored in `csl` files, which can be downloaded through `md-pdf`. See the usage instructions on how to download these.

There's a full list of available `csl` files [here](https://github.com/citation-style-language/styles/).

## Example
Assuming youre using the same bibliography as the example, an input of:

```markdown
@item1 says blah.
```
Will render as:
```
Doe (2005) says blah.
```

### Advanced Citation
You can also use more advanced referencing to be more specific:
```markdown
A citation group [see @item1 p. 34-35; also @item3 chap. 3].
```
will result in:
```
A citation group (see Doe 2005, 34–35; also Doe and Roe 2007, chap. 3)
```
