What precision (P@1) were you able to achieve?

The first shot was P@1 0.121, with 25 epochs and lr P@1 0.632 but P@5 0.163. With the pruned setup P@1 0.967

What fastText parameters did you use?

fasttext supervised -input pruned_train.txt -epoch 25 -output model_pruned -wordNgrams 2 -lr 1

How did you transform the product names?

I did not touch this transformation, since the text indicated that the data is already normalized. A look into the data confirmed this.

How did you prune infrequent category labels, and how did that affect your precision?

I have written a python script which removed labels with a low amount of samples (less than 500). It has raised the precision and lowered the training time.

How did you prune the category tree, and how did that affect your precision?

Not tackled.

For deriving synonyms from content:

What were the results for your best model in the tokens used for evaluation?

`
Query word? headphones
earbud 0.879971
headphone 0.847561
ear 0.838008
lowrider 0.671399
earphones 0.663913
over 0.656692
bud 0.642849
ihip 0.626942
canceling 0.619071
behind 0.618874
Query word? laptop
netbook 0.683992
notebook 0.676387
briefcase 0.623729
laptops 0.577275
ultrabook 0.547828
mouse 0.538457
netbooks 0.525811
notebooks 0.520422
pavilion 0.515945
slip 0.511098
Query word? freezer
refrigerator 0.708265
cu 0.657123
mug 0.644617
ft 0.628171
frost 0.617115
satina 0.599452
side 0.576935
cleansteel 0.566712
refrigerators 0.561573
monochromatic 0.552278
Query word? nintendo
ds 0.955419
wii 0.949211
3ds 0.81399
psp 0.767625
gamecube 0.764917
xbox 0.745169
advance 0.73057
boy 0.729339
playstation 0.728873
360 0.722177
Query word? whirlpool
maytag 0.775467
biscuit 0.754001
frigidaire 0.732445
ge 0.711445
inglis 0.695252
bisque 0.684194
hotpoint 0.672437
gas 0.632224
cleansteel 0.631452
cu 0.618102
Query word? kodak
easyshare 0.825965
m863 0.653414
playsport 0.640963
m1063 0.636892
m893 0.631252
esp 0.62073
m340 0.613225
playtouch 0.605451
photosmart 0.558506
canon 0.555659
Query word? ps2
gamecube 0.758271
gba 0.726195
playstation 0.723197
ps3 0.721673
guide 0.715827
xbox 0.712251
360 0.667502
psp 0.641931
cheats 0.633677
game 0.624732
Query word? razr
motorola 0.76948
droid 0.701371
nokia 0.666081
cell 0.650526
8530 0.637372
phones 0.637126
atrix 0.624291
8520 0.589809
palm 0.581705
xoom 0.580385
Query word? stratocaster
telecaster 0.862093
strat 0.778766
squier 0.770452
fender 0.750586
fretboard 0.747372
rosewood 0.61781
sunburst 0.617452
mustang 0.606693
jazz 0.565757
bass 0.555024
Query word? holiday
hanukkah 0.605543
happy 0.575862
graduation 0.575381
gift 0.569763
kwanzaa 0.568163
buy 0.568123
thank 0.567706
congratulations 0.565624
best 0.545626
navidad 0.539717
Query word? plasma
600hz 0.730732
hdtv 0.648583
screens 0.588307
viera 0.586387
42 0.56965
dlp 0.564519
class 0.563309
58 0.560462
120hz 0.542892
hdtvs 0.541012
Query word? leather
armless 0.663842
sofa 0.63784
recliner 0.633365
curved 0.608047
berkline 0.59632
case 0.591918
seating 0.58083
bodhi 0.572367
theaterseatstore 0.548685
kenneth 0.537892
`

What fastText parameters did you use?

~/fastText-0.9.2/fasttext skipgram -input /workspace/datasets/fasttext/normalized_filtered_titles.txt -epoch 25 -output /workspace/datasets/fasttext/title_model -minCount 20

How did you transform the product names?

Purged non-ascii characters and transformed everything into lowercase.

For integrating synonyms with search:

How did you transform the product names (if different than previously)?

Same as before with added filter of minimum length of 4 characters.

What threshold score did you use?

0.75

Were you able to find the additional results by matching synonyms?

Yes, it has shown that the recall improves with the introduction of synonyms. However, due to my chosen threshold the results were slightly different or even in the case of nesspresso the same as without synonyms.