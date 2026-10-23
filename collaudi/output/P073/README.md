# P073 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P073/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · unittest_project_suite

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "run_tests.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 111 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
SEED_RESULT {"baseline_mae": 5.143100214119276, "baseline_rmse": 6.185825882879108, "mae": 0.9516339552504062, "raw_temperature_mae": 3.732018337888156, "rmse": 1.1738899057053347, "seed": 0}
SEED_RESULT {"baseline_mae": 4.095716610635033, "baseline_rmse": 5.307216232302876, "mae": 1.2111134781047046, "raw_temperature_mae": 3.5717463371168345, "rmse": 1.487974049131613, "seed": 1}
SEED_RESULT {"baseline_mae": 4.022166279604893, "baseline_rmse": 5.2401088934769655, "mae": 0.9987928172710544, "raw_temperature_mae": 3.286594053952093, "rmse": 1.2646771928864005, "seed": 2}
SEED_RESULT {"baseline_mae": 5.71264090141976, "baseline_rmse": 6.872930886423136, "mae": 0.9426854771150115, "raw_temperature_mae": 3.945843529527911, "rmse": 1.202158848739022, "seed": 3}
SEED_RESULT {"baseline_mae": 4.029868381782944, "baseline_rmse": 4.973104601747838, "mae": 1.0111462866052296, "raw_temperature_mae": 3.324001500705762, "rmse": 1.2556254121093393, "seed": 4}
SEED_RESULT {"baseline_mae": 4.867545666134796, "baseline_rmse": 5.96292560366185, "mae": 0.9592364431080012, "raw_temperature_mae": 3.336792145999371, "rmse": 1.1818593388821954, "seed": 5}
SEED_RESULT {"baseline_mae": 5.523029777311799, "baseline_rmse": 6.418110386315137, "mae": 0.9068567432078993, "raw_temperature_mae": 3.3091604478322876, "rmse": 1.0767510558924103, "seed": 6}
SEED_RESULT {"baseline_mae": 5.284453913625479, "baseline_rmse": 6.401147741516269, "mae": 0.9989184289217466, "raw_temperature_mae": 3.497307445391551, "rmse": 1.2575652980087821, "seed": 7}
SEED_RESULT {"baseline_mae": 5.252965351464312, "baseline_rmse": 6.3593201724601744, "mae": 1.086960550423837, "raw_temperature_mae": 3.5341288418848635, "rmse": 1.3784289548499884, "seed": 8}
SEED_RESULT {"baseline_mae": 3.4449902286516827, "baseline_rmse": 4.407783466454878, "mae": 0.8551027261412891, "raw_temperature_mae": 3.1360096656388183, "rmse": 1.067808598720892, "seed": 9}
SEED_RESULT {"baseline_mae": 4.7961225506215674, "baseline_rmse": 5.841891189916554, "mae": 0.914614018019847, "raw_temperature_mae": 3.584735578571256, "rmse": 1.1693723665436573, "seed": 10}
SEED_RESULT {"baseline_mae": 5.556305061141461, "baseline_rmse": 6.449200762651129, "mae": 1.1007262300342435, "raw_temperature_mae": 3.9441216889595183, "rmse": 1.3829842701827606, "seed": 11}
SEED_RESULT {"baseline_mae": 4.982481644180057, "baseline_rmse": 5.921355683735598, "mae": 0.9663534825358345, "raw_temperature_mae": 3.5712250195058717, "rmse": 1.1728255509483498, "seed": 12}
SEED_RESULT {"baseline_mae": 4.919814681245149, "baseline_rmse": 5.975386102460796, "mae": 0.8459139893697696, "raw_temperature_mae": 3.206790200097736, "rmse": 1.0900490282331037, "seed": 13}
SEED_RESULT {"baseline_mae": 5.13117253373041, "baseline_rmse": 6.516122999034175, "mae": 0.9717566595705741, "raw_temperature_mae": 3.345194012269593, "rmse": 1.263674720980243, "seed": 14}
SEED_RESULT {"baseline_mae": 4.514174461565148, "baseline_rmse": 5.7022176755944045, "mae": 0.835661347084784, "raw_temperature_mae": 3.6096741967980845, "rmse": 1.035430557898046, "seed": 15}
SEED_RESULT {"baseline_mae": 4.739812196674629, "baseline_rmse": 6.041185035092493, "mae": 0.9145926408450752, "raw_temperature_mae": 3.3563949489620684, "rmse": 1.1279637666772273, "seed": 16}
SEED_RESULT {"baseline_mae": 4.887498630225607, "baseline_rmse": 5.911890882096604, "mae": 0.9890591566417807, "raw_temperature_mae": 3.4114959704749808, "rmse": 1.205205505928547, "seed": 17}
SEED_RESULT {"baseline_mae": 4.5339594840817705, "baseline_rmse": 5.545795878674698, "mae": 0.8961294003709969, "raw_temperature_mae": 3.7245805224852737, "rmse": 1.0960246582299507, "seed": 18}
SEED_RESULT {"baseline_mae": 4.322317626173072, "baseline_rmse": 5.4595564498282405, "mae": 0.9153910283404393, "raw_temperature_mae": 3.4221235684196283, "rmse": 1.1080374459334643, "seed": 19}
SEED_RESULT {"baseline_mae": 4.920917219277524, "baseline_rmse": 5.857447413241629, "mae": 0.9806244040345139, "raw_temperature_mae": 3.4242212336611026, "rmse": 1.2454663549484708, "seed": 20}
SEED_RESULT {"baseline_mae": 5.049120580594818, "baseline_rmse": 6.099933607818286, "mae": 0.9705211180692639, "raw_temperature_mae": 3.2198310284729454, "rmse": 1.2391936337782399, "seed": 21}
SEED_RESULT {"baseline_mae": 5.647838944355681, "baseline_rmse": 6.650415058664999, "mae": 1.0405728638402045, "raw_temperature_mae": 3.351383697478001, "rmse": 1.3694650601423108, "seed": 22}
SEED_RESULT {"baseline_mae": 4.6120234738200345, "baseline_rmse": 5.571619416807098, "mae": 1.1812782234835373, "raw_temperature_mae": 3.215281069897579, "rmse": 1.3955301567017298, "seed": 23}
SEED_RESULT {"baseline_mae": 5.7580261730361295, "baseline_rmse": 6.854609569852963, "mae": 0.8841891317210018, "raw_temperature_mae": 3.609083993706692, "rmse": 1.1307833944471783, "seed": 24}
SEED_RESULT {"baseline_mae": 4.709467671495626, "baseline_rmse": 5.805836841186714, "mae": 0.9604070529772926, "raw_temperature_mae": 4.247787627836804, "rmse": 1.2204957440646749, "seed": 25}
SEED_RESULT {"baseline_mae": 5.1516085526983, "baseline_rmse": 6.263140642761082, "mae": 1.1759126545370517, "raw_temperature_mae": 3.7813399973992547, "rmse": 1.5221565907369043, "seed": 26}
SEED_RESULT {"baseline_mae": 4.683959414707529, "baseline_rmse": 5.896125576433905, "mae": 1.1293192599741613, "raw_temperature_mae": 3.933835994543694, "rmse": 1.3203803696388514, "seed": 27}
SEED_RESULT {"baseline_mae": 5.233883279971464, "baseline_rmse": 6.401569935045663, "mae": 1.0435841556068126, "raw_temperature_mae": 3.765134087491323, "rmse": 1.272080323290599, "seed": 28}
SEED_RESULT {"baseline_mae": 5.045968947510219, "baseline_rmse": 5.952794610669471, "mae": 1.128658168436331, "raw_temperature_mae": 2.956704631363327, "rmse": 1.3765096892590991, "seed": 29}
SEED_RESULT {"baseline_mae": 5.746007187015048, "baseline_rmse": 6.923648784252871, "mae": 1.161619227671357, "raw_temperature_mae": 3.896344258887072, "rmse": 1.4336687629040235, "seed": 30}
SEED_RESULT {"baseline_mae": 5.019426850411315, "baseline_rmse": 6.209118312762712, "mae": 0.9170405313391492, "raw_temperature_mae": 3.579006475687436, "rmse": 1.1890063313455879, "seed": 31}
SEED_RESULT {"baseline_mae": 4.464784160792608, "baseline_rmse": 5.7940781251063465, "mae": 0.9870911905301673, "raw_temperature_mae": 3.432268887517963, "rmse": 1.2367081513026237, "seed": 32}
SEED_RESULT {"baseline_mae": 4.904867872621409, "baseline_rmse": 5.929797482737257, "mae": 1.0320910859273578, "raw_temperature_mae": 3.475806237829206, "rmse": 1.289647345376413, "seed": 33}
SEED_RESULT {"baseline_mae": 5.143342290600317, "baseline_rmse": 6.080209695564452, "mae": 0.8751640078478512, "raw_temperature_mae": 3.458946098897144, "rmse": 1.1123846030253701, "seed": 34}
SEED_RESULT {"baseline_mae": 6.020197366715703, "baseline_rmse": 7.014562827679866, "mae": 0.9057633324893656, "raw_temperature_mae": 3.824927915963071, "rmse": 1.0824726464282837, "seed": 35}
SEED_RESULT {"baseline_mae": 4.625323088806279, "baseline_rmse": 5.5118721420425665, "mae": 0.9052723203807544, "raw_temperature_mae": 3.1180433691204623, "rmse": 1.1062404639343815, "seed": 36}
SEED_RESULT {"baseline_mae": 4.632617832422179, "baseline_rmse": 5.742022167890706, "mae": 0.9607051154784754, "raw_temperature_mae": 3.2332608782494905, "rmse": 1.1870378119633909, "seed": 37}
SEED_RESULT {"baseline_mae": 5.036887010719861, "baseline_rmse": 5.955405385476315, "mae": 1.0250999081871, "raw_temperature_mae": 3.2845159957514056, "rmse": 1.2371229038336806, "seed": 38}
SEED_RESULT {"baseline_mae": 4.672619975798435, "baseline_rmse": 5.893306746083763, "mae": 1.0584899353616255, "raw_temperature_mae": 3.563441296762922, "rmse": 1.2678707469765431, "seed": 39}
SEED_RESULT {"baseline_mae": 5.069357575449144, "baseline_rmse": 6.3754651672450375, "mae": 1.0253145544303661, "raw_temperature_mae": 3.4878132027791797, "rmse": 1.3565509339307211, "seed": 40}
SEED_RESULT {"baseline_mae": 5.433540576795765, "baseline_rmse": 6.531856215001094, "mae": 0.9055835350045022, "raw_temperature_mae": 3.549990391305754, "rmse": 1.214067825916683, "seed": 41}
SEED_RESULT {"baseline_mae": 4.420412003443908, "baseline_rmse": 5.412714204475421, "mae": 0.9990538929841493, "raw_temperature_mae": 3.450953436172233, "rmse": 1.273172792041718, "seed": 42}
SEED_RESULT {"baseline_mae": 4.567113450699934, "baseline_rmse": 5.9262148342588725, "mae": 1.075801643692839, "raw_temperature_mae": 3.705505186925941, "rmse": 1.305116662323214, "seed": 43}
SEED_RESULT {"baseline_mae": 4.9332121393350405, "baseline_rmse": 5.733479001427359, "mae": 1.0913549049360076, "raw_temperature_mae": 2.798372836272618, "rmse": 1.321003157205923, "seed": 44}
SEED_RESULT {"baseline_mae": 4.759402611699366, "baseline_rmse": 5.7242475849644014, "mae": 1.0257313949984612, "raw_temperature_mae": 4.052879633961341, "rmse": 1.272982849692189, "seed": 45}
SEED_RESULT {"baseline_mae": 4.811587668385703, "baseline_rmse": 5.643576793626152, "mae": 1.013727102681227, "raw_temperature_mae": 3.439084304469454, "rmse": 1.3120568805135255, "seed": 46}
SEED_RESULT {"baseline_mae": 5.580319192082899, "baseline_rmse": 6.5885173415254386, "mae": 0.995069478172806, "raw_temperature_mae": 3.434245917069257, "rmse": 1.2758668348690017, "seed": 47}
SEED_RESULT {"baseline_mae": 4.537778397235666, "baseline_rmse": 5.574895933926141, "mae": 1.028347718131177, "raw_temperature_mae": 3.358262643810684, "rmse": 1.249630442683182, "seed": 48}
SEED_RESULT {"baseline_mae": 4.3854060733311355, "baseline_rmse": 5.420258270707132, "mae": 1.0613077188530318, "raw_temperature_mae": 3.116958934327965, "rmse": 1.3175491443168659, "seed": 49}
SEED_RESULT {"baseline_mae": 5.138792805728994, "baseline_rmse": 6.247643514210009, "mae": 0.991724834566769, "raw_temperature_mae": 3.489934959183022, "rmse": 1.2170338399347047, "seed": 50}
SEED_RESULT {"baseline_mae": 4.0751928398992225, "baseline_rmse": 5.272043016445366, "mae": 0.921944792013289, "raw_temperature_mae": 3.838697750384264, "rmse": 1.135988860336752, "seed": 51}
SEED_RESULT {"baseline_mae": 4.6726283876626376, "baseline_rmse": 5.932478979897613, "mae": 0.8654397500236666, "raw_temperature_mae": 3.2673261908595435, "rmse": 1.1346305345550678, "seed": 52}
SEED_RESULT {"baseline_mae": 5.608199125598008, "baseline_rmse": 6.7261310874149185, "mae": 1.09204127284019, "raw_temperature_mae": 3.7871912569793165, "rmse": 1.374269483089231, "seed": 53}
SEED_RESULT {"baseline_mae": 5.081654240415071, "baseline_rmse": 6.224739604871144, "mae": 1.0970754835221308, "raw_temperature_mae": 3.854402098749106, "rmse": 1.3074313959541035, "seed": 54}
SEED_RESULT {"baseline_mae": 5.535077045532882, "baseline_rmse": 6.59739823785431, "mae": 1.0520078119694822, "raw_temperature_mae": 3.780595632451482, "rmse": 1.2461447375852805, "seed": 55}
SEED_RESULT {"baseline_mae": 5.442305449414009, "baseline_rmse": 6.752963568225802, "mae": 0.9824640054326628, "raw_temperature_mae": 3.653303263586918, "rmse": 1.2522559495512788, "seed": 56}
SEED_RESULT {"baseline_mae": 5.581349838542002, "baseline_rmse": 6.585121639996658, "mae": 0.8901965179650083, "raw_temperature_mae": 3.2476710992327544, "rmse": 1.107854940456907, "seed": 57}
SEED_RESULT {"baseline_mae": 4.762915421371556, "baseline_rmse": 5.937011747551529, "mae": 1.051039312812727, "raw_temperature_mae": 3.467569773385064, "rmse": 1.261050850336822, "seed": 58}
SEED_RESULT {"baseline_mae": 5.06532683307796, "baseline_rmse": 6.021043077790629, "mae": 0.9539107971370434, "raw_temperature_mae": 3.4828165509135323, "rmse": 1.09850675498389, "seed": 59}
SEED_RESULT {"baseline_mae": 5.504521779957003, "baseline_rmse": 6.584590411316814, "mae": 1.0658522111557394, "raw_temperature_mae": 3.6002404721615324, "rmse": 1.3581632167265276, "seed": 60}
SEED_RESULT {"baseline_mae": 4.126851126950178, "baseline_rmse": 5.221870898982192, "mae": 0.9595919616721932, "raw_temperature_mae": 3.68526779291212, "rmse": 1.235281750091023, "seed": 61}
SEED_RESULT {"baseline_mae": 4.779361934372476, "baseline_rmse": 6.064238361638681, "mae": 0.8440451416719648, "raw_temperature_mae": 3.8337605146379237, "rmse": 1.029171373139825, "seed": 62}
SEED_RESULT {"baseline_mae": 5.914911297062021, "baseline_rmse": 6.7627571304355865, "mae": 1.0541272648882656, "raw_temperature_mae": 3.7379430305902437, "rmse": 1.3239900324425578, "seed": 63}
SEED_RESULT {"baseline_mae": 4.471553444137308, "baseline_rmse": 5.664711957516417, "mae": 1.0101274361752455, "raw_temperature_mae": 3.6894917494498847, "rmse": 1.2482623867647993, "seed": 64}
SEED_RESULT {"baseline_mae": 5.464523061003345, "baseline_rmse": 6.708174165190904, "mae": 0.9369889227689465, "raw_temperature_mae": 3.958104683804442, "rmse": 1.1218214383860998, "seed": 65}
SEED_RESULT {"baseline_mae": 3.9637979683506552, "baseline_rmse": 5.205048261441454, "mae": 1.1210242084371942, "raw_temperature_mae": 3.4952994055219895, "rmse": 1.3428912766017764, "seed": 66}
SEED_RESULT {"baseline_mae": 5.000744810032078, "baseline_rmse": 5.856248276858286, "mae": 1.0138686732194624, "raw_temperature_mae": 3.5017311102093784, "rmse": 1.226645096100187, "seed": 67}
SEED_RESULT {"baseline_mae": 4.450850865138709, "baseline_rmse": 5.357600674999939, "mae": 1.0255540477802956, "raw_temperature_mae": 3.5905957152953323, "rmse": 1.245889015517009, "seed": 68}
SEED_RESULT {"baseline_mae": 4.918286586939729, "baseline_rmse": 5.871995685128678, "mae": 0.9775570285827713, "raw_temperature_mae": 3.5888895036579265, "rmse": 1.2507962439582219, "seed": 69}
SEED_RESULT {"baseline_mae": 4.662940856215115, "baseline_rmse": 5.7607805462772514, "mae": 0.9928373161197421, "raw_temperature_mae": 3.1215224393741603, "rmse": 1.2537795948131714, "seed": 70}
SEED_RESULT {"baseline_mae": 5.484402852071158, "baseline_rmse": 6.449774929497745, "mae": 0.7916564835242286, "raw_temperature_mae": 3.5034007514766468, "rmse": 0.9828449009049856, "seed": 71}
SEED_RESULT {"baseline_mae": 5.436502071026989, "baseline_rmse": 6.819824860121142, "mae": 0.9155607966998732, "raw_temperature_mae": 3.5657716584643384, "rmse": 1.1832400449380276, "seed": 72}
SEED_RESULT {"baseline_mae": 5.1079775943694035, "baseline_rmse": 6.245616126684605, "mae": 0.9008333272825605, "raw_temperature_mae": 3.1912260281845493, "rmse": 1.114662807269924, "seed": 73}
SEED_RESULT {"baseline_mae": 5.455635639489296, "baseline_rmse": 6.266094110205769, "mae": 0.85307579082974, "raw_temperature_mae": 3.505951359040109, "rmse": 1.1206787930221418, "seed": 74}
SEED_RESULT {"baseline_mae": 4.446940940147692, "baseline_rmse": 5.310787219576733, "mae": 1.0145069664914879, "raw_temperature_mae": 3.407255206665471, "rmse": 1.2148123886597517, "seed": 75}
SEED_RESULT {"baseline_mae": 5.1188772259279025, "baseline_rmse": 6.399007879497962, "mae": 1.0243413673484074, "raw_temperature_mae": 3.5549671303188792, "rmse": 1.2454589061592474, "seed": 76}
SEED_RESULT {"baseline_mae": 4.837027126719314, "baseline_rmse": 5.77709641893092, "mae": 1.0187896548717186, "raw_temperature_mae": 3.172128654897471, "rmse": 1.2369025124916304, "seed": 77}
SEED_RESULT {"baseline_mae": 3.9996725793322865, "baseline_rmse": 5.127882004276508, "mae": 0.7647453059877626, "raw_temperature_mae": 3.494319903851135, "rmse": 0.9701126311335365, "seed": 78}
SEED_RESULT {"baseline_mae": 4.1738148734245, "baseline_rmse": 5.335941540362687, "mae": 1.1571429846466854, "raw_temperature_mae": 3.2743941163180095, "rmse": 1.3763418957653901, "seed": 79}
SEED_RESULT {"baseline_mae": 4.85110870916843, "baseline_rmse": 5.913423154456136, "mae": 0.9364090959306932, "raw_temperature_mae": 3.636844061215436, "rmse": 1.2472976533748805, "seed": 80}
SEED_RESULT {"baseline_mae": 4.63108557677649, "baseline_rmse": 5.893453285061814, "mae": 0.8811106403066884, "raw_temperature_mae": 3.815722527351699, "rmse": 1.0627755071614313, "seed": 81}
SEED_RESULT {"baseline_mae": 4.768443475720687, "baseline_rmse": 5.664271331615573, "mae": 0.7505492951569107, "raw_temperature_mae": 2.8190962608415604, "rmse": 0.9912396047874452, "seed": 82}
SEED_RESULT {"baseline_mae": 4.009657996258897, "baseline_rmse": 5.1799845633116135, "mae": 1.075863521267216, "raw_temperature_mae": 3.746963494229838, "rmse": 1.3717675625030625, "seed": 83}
SEED_RESULT {"baseline_mae": 4.7682927044488075, "baseline_rmse": 6.054355327769172, "mae": 0.8211040602666474, "raw_temperature_mae": 3.566875156170469, "rmse": 1.0495301495375744, "seed": 84}
SEED_RESULT {"baseline_mae": 4.730275938024212, "baseline_rmse": 5.634141809382483, "mae": 0.9046201928291845, "raw_temperature_mae": 3.0142201330912597, "rmse": 1.1662621291899558, "seed": 85}
SEED_RESULT {"baseline_mae": 5.136816344578606, "baseline_rmse": 6.251312247072234, "mae": 1.1556403827837858, "raw_temperature_mae": 3.9742676358904996, "rmse": 1.4252378643925918, "seed": 86}
SEED_RESULT {"baseline_mae": 4.743901367511252, "baseline_rmse": 5.789318263338248, "mae": 0.9801821918004038, "raw_temperature_mae": 3.590848496119389, "rmse": 1.2817692664875315, "seed": 87}
SEED_RESULT {"baseline_mae": 5.1249604659386385, "baseline_rmse": 6.158108308778348, "mae": 0.8681007303623898, "raw_temperature_mae": 3.6663266998185753, "rmse": 1.0660191597935844, "seed": 88}
SEED_RESULT {"baseline_mae": 4.720268545904461, "baseline_rmse": 5.847952409205176, "mae": 1.0010747822142727, "raw_temperature_mae": 3.8562816100098676, "rmse": 1.3094845265449393, "seed": 89}
SEED_RESULT {"baseline_mae": 5.1496798457781985, "baseline_rmse": 6.168865269172818, "mae": 0.7991255230787709, "raw_temperature_mae": 3.357681516609369, "rmse": 1.0378499387845195, "seed": 90}
SEED_RESULT {"baseline_mae": 5.033599396435331, "baseline_rmse": 6.196477745665542, "mae": 0.9415898358123418, "raw_temperature_mae": 3.6692347514068704, "rmse": 1.1623246081916772, "seed": 91}
SEED_RESULT {"baseline_mae": 4.742040776922263, "baseline_rmse": 5.757363506434276, "mae": 0.7954905152746695, "raw_temperature_mae": 3.0015057907231313, "rmse": 1.0058937722014518, "seed": 92}
SEED_RESULT {"baseline_mae": 5.365311070522995, "baseline_rmse": 6.344005774769428, "mae": 0.9213183091600938, "raw_temperature_mae": 3.3407620410590066, "rmse": 1.1159337827370917, "seed": 93}
SEED_RESULT {"baseline_mae": 5.03231787191486, "baseline_rmse": 6.175262168974339, "mae": 0.9713197508835533, "raw_temperature_mae": 3.6609766823255976, "rmse": 1.1570427477520258, "seed": 94}
SEED_RESULT {"baseline_mae": 4.580276951423945, "baseline_rmse": 5.5107211749444, "mae": 0.9116975079937667, "raw_temperature_mae": 3.4721038320472943, "rmse": 1.1485067296223104, "seed": 95}
SEED_RESULT {"baseline_mae": 4.8181430997372585, "baseline_rmse": 5.88822919815678, "mae": 0.8620033099309042, "raw_temperature_mae": 3.427146503443669, "rmse": 1.0833903935914697, "seed": 96}
SEED_RESULT {"baseline_mae": 3.6965836151032065, "baseline_rmse": 4.894113306898451, "mae": 0.9716898135402412, "raw_temperature_mae": 3.3658338110003125, "rmse": 1.190133206199986, "seed": 97}
SEED_RESULT {"baseline_mae": 4.073744545949031, "baseline_rmse": 4.990350296129931, "mae": 0.9526452232508535, "raw_temperature_mae": 3.463393982944362, "rmse": 1.1263954340809692, "seed": 98}
SEED_RESULT {"baseline_mae": 4.795000746510426, "baseline_rmse": 5.705845070767911, "mae": 1.042980995361179, "raw_temperature_mae": 3.2277337112806377, "rmse": 1.254828771771363, "seed": 99}
TEST_SUMMARY {"tests_run": 111, "failures": 0, "errors": 0, "skipped": 0, "successful": true}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_changed_training_targets_change_model (test_p073.EnergyContracts.test_changed_training_targets_change_model) ... ok
test_default_model_beats_predeclared_baselines (test_p073.EnergyContracts.test_default_model_beats_predeclared_baselines) ... ok
test_determinism (test_p073.EnergyContracts.test_determinism) ... ok
test_invalid_X (test_p073.EnergyContracts.test_invalid_X) ... ok
test_invalid_generator_and_split (test_p073.EnergyContracts.test_invalid_generator_and_split) ... ok
test_invalid_metric_inputs (test_p073.EnergyContracts.test_invalid_metric_inputs) ... ok
test_invalid_targets (test_p073.EnergyContracts.test_invalid_targets) ... ok
test_metric_hand_calculation (test_p073.EnergyContracts.test_metric_hand_calculation) ... ok
test_no_test_rows_or_targets_in_fit (test_p073.EnergyContracts.test_no_test_rows_or_targets_in_fit) ... ok
test_noiseless_known_coefficients (test_p073.EnergyContracts.test_noiseless_known_coefficients) ... ok
test_symmetric_temperature_feature (test_p073.EnergyContracts.test_symmetric_temperature_feature) ... ok
test_seed_000 (test_p073.SeededOracleChecks.test_seed_000) ... ok
test_seed_001 (test_p073.SeededOracleChecks.test_seed_001) ... ok
test_seed_002 (test_p073.SeededOracleChecks.test_seed_002) ... ok
test_seed_003 (test_p073.SeededOracleChecks.test_seed_003) ... ok
test_seed_004 (test_p073.SeededOracleChecks.test_seed_004) ... ok
test_seed_005 (test_p073.SeededOracleChecks.test_seed_005) ... ok
test_seed_006 (test_p073.SeededOracleChecks.test_seed_006) ... ok
test_seed_007 (test_p073.SeededOracleChecks.test_seed_007) ... ok
test_seed_008 (test_p073.SeededOracleChecks.test_seed_008) ... ok
test_seed_009 (test_p073.SeededOracleChecks.test_seed_009) ... ok
test_seed_010 (test_p073.SeededOracleChecks.test_seed_010) ... ok
test_seed_011 (test_p073.SeededOracleChecks.test_seed_011) ... ok
test_seed_012 (test_p073.SeededOracleChecks.test_seed_012) ... ok
test_seed_013 (test_p073.SeededOracleChecks.test_seed_013) ... ok
test_seed_014 (test_p073.SeededOracleChecks.test_seed_014) ... ok
test_seed_015 (test_p073.SeededOracleChecks.test_seed_015) ... ok
test_seed_016 (test_p073.SeededOracleChecks.test_seed_016) ... ok
test_seed_017 (test_p073.SeededOracleChecks.test_seed_017) ... ok
test_seed_018 (test_p073.SeededOracleChecks.test_seed_018) ... ok
test_seed_019 (test_p073.SeededOracleChecks.test_seed_019) ... ok
test_seed_020 (test_p073.SeededOracleChecks.test_seed_020) ... ok
test_seed_021 (test_p073.SeededOracleChecks.test_seed_021) ... ok
test_seed_022 (test_p073.SeededOracleChecks.test_seed_022) ... ok
test_seed_023 (test_p073.SeededOracleChecks.test_seed_023) ... ok
test_seed_024 (test_p073.SeededOracleChecks.test_seed_024) ... ok
test_seed_025 (test_p073.SeededOracleChecks.test_seed_025) ... ok
test_seed_026 (test_p073.SeededOracleChecks.test_seed_026) ... ok
test_seed_027 (test_p073.SeededOracleChecks.test_seed_027) ... ok
test_seed_028 (test_p073.SeededOracleChecks.test_seed_028) ... ok
test_seed_029 (test_p073.SeededOracleChecks.test_seed_029) ... ok
test_seed_030 (test_p073.SeededOracleChecks.test_seed_030) ... ok
test_seed_031 (test_p073.SeededOracleChecks.test_seed_031) ... ok
test_seed_032 (test_p073.SeededOracleChecks.test_seed_032) ... ok
test_seed_033 (test_p073.SeededOracleChecks.test_seed_033) ... ok
test_seed_034 (test_p073.SeededOracleChecks.test_seed_034) ... ok
test_seed_035 (test_p073.SeededOracleChecks.test_seed_035) ... ok
test_seed_036 (test_p073.SeededOracleChecks.test_seed_036) ... ok
test_seed_037 (test_p073.SeededOracleChecks.test_seed_037) ... ok
test_seed_038 (test_p073.SeededOracleChecks.test_seed_038) ... ok
test_seed_039 (test_p073.SeededOracleChecks.test_seed_039) ... ok
test_seed_040 (test_p073.SeededOracleChecks.test_seed_040) ... ok
test_seed_041 (test_p073.SeededOracleChecks.test_seed_041) ... ok
test_seed_042 (test_p073.SeededOracleChecks.test_seed_042) ... ok
test_seed_043 (test_p073.SeededOracleChecks.test_seed_043) ... ok
test_seed_044 (test_p073.SeededOracleChecks.test_seed_044) ... ok
test_seed_045 (test_p073.SeededOracleChecks.test_seed_045) ... ok
test_seed_046 (test_p073.SeededOracleChecks.test_seed_046) ... ok
test_seed_047 (test_p073.SeededOracleChecks.test_seed_047) ... ok
test_seed_048 (test_p073.SeededOracleChecks.test_seed_048) ... ok
test_seed_049 (test_p073.SeededOracleChecks.test_seed_049) ... ok
test_seed_050 (test_p073.SeededOracleChecks.test_seed_050) ... ok
test_seed_051 (test_p073.SeededOracleChecks.test_seed_051) ... ok
test_seed_052 (test_p073.SeededOracleChecks.test_seed_052) ... ok
test_seed_053 (test_p073.SeededOracleChecks.test_seed_053) ... ok
test_seed_054 (test_p073.SeededOracleChecks.test_seed_054) ... ok
test_seed_055 (test_p073.SeededOracleChecks.test_seed_055) ... ok
test_seed_056 (test_p073.SeededOracleChecks.test_seed_056) ... ok
test_seed_057 (test_p073.SeededOracleChecks.test_seed_057) ... ok
test_seed_058 (test_p073.SeededOracleChecks.test_seed_058) ... ok
test_seed_059 (test_p073.SeededOracleChecks.test_seed_059) ... ok
test_seed_060 (test_p073.SeededOracleChecks.test_seed_060) ... ok
test_seed_061 (test_p073.SeededOracleChecks.test_seed_061) ... ok
test_seed_062 (test_p073.SeededOracleChecks.test_seed_062) ... ok
test_seed_063 (test_p073.SeededOracleChecks.test_seed_063) ... ok
test_seed_064 (test_p073.SeededOracleChecks.test_seed_064) ... ok
test_seed_065 (test_p073.SeededOracleChecks.test_seed_065) ... ok
test_seed_066 (test_p073.SeededOracleChecks.test_seed_066) ... ok
test_seed_067 (test_p073.SeededOracleChecks.test_seed_067) ... ok
test_seed_068 (test_p073.SeededOracleChecks.test_seed_068) ... ok
test_seed_069 (test_p073.SeededOracleChecks.test_seed_069) ... ok
test_seed_070 (test_p073.SeededOracleChecks.test_seed_070) ... ok
test_seed_071 (test_p073.SeededOracleChecks.test_seed_071) ... ok
test_seed_072 (test_p073.SeededOracleChecks.test_seed_072) ... ok
test_seed_073 (test_p073.SeededOracleChecks.test_seed_073) ... ok
test_seed_074 (test_p073.SeededOracleChecks.test_seed_074) ... ok
test_seed_075 (test_p073.SeededOracleChecks.test_seed_075) ... ok
test_seed_076 (test_p073.SeededOracleChecks.test_seed_076) ... ok
test_seed_077 (test_p073.SeededOracleChecks.test_seed_077) ... ok
test_seed_078 (test_p073.SeededOracleChecks.test_seed_078) ... ok
test_seed_079 (test_p073.SeededOracleChecks.test_seed_079) ... ok
test_seed_080 (test_p073.SeededOracleChecks.test_seed_080) ... ok
test_seed_081 (test_p073.SeededOracleChecks.test_seed_081) ... ok
test_seed_082 (test_p073.SeededOracleChecks.test_seed_082) ... ok
test_seed_083 (test_p073.SeededOracleChecks.test_seed_083) ... ok
test_seed_084 (test_p073.SeededOracleChecks.test_seed_084) ... ok
test_seed_085 (test_p073.SeededOracleChecks.test_seed_085) ... ok
test_seed_086 (test_p073.SeededOracleChecks.test_seed_086) ... ok
test_seed_087 (test_p073.SeededOracleChecks.test_seed_087) ... ok
test_seed_088 (test_p073.SeededOracleChecks.test_seed_088) ... ok
test_seed_089 (test_p073.SeededOracleChecks.test_seed_089) ... ok
test_seed_090 (test_p073.SeededOracleChecks.test_seed_090) ... ok
test_seed_091 (test_p073.SeededOracleChecks.test_seed_091) ... ok
test_seed_092 (test_p073.SeededOracleChecks.test_seed_092) ... ok
test_seed_093 (test_p073.SeededOracleChecks.test_seed_093) ... ok
test_seed_094 (test_p073.SeededOracleChecks.test_seed_094) ... ok
test_seed_095 (test_p073.SeededOracleChecks.test_seed_095) ... ok
test_seed_096 (test_p073.SeededOracleChecks.test_seed_096) ... ok
test_seed_097 (test_p073.SeededOracleChecks.test_seed_097) ... ok
test_seed_098 (test_p073.SeededOracleChecks.test_seed_098) ... ok
test_seed_099 (test_p073.SeededOracleChecks.test_seed_099) ... ok

----------------------------------------------------------------------
Ran 111 tests in 0.105s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_energy_regression

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/energy_regression.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_energy_regression.stdout.txt)

```text
P073 — 180 esempi di training; 60 esempi di test sintetici
mae: 0.998918
rmse: 1.257565
baseline_mae: 5.284454
baseline_rmse: 6.401148
raw_temperature_mae: 3.497307
intercetta: 17.883517
coefficienti: 0.782513, 8.464744, 0.070671
prima previsione: 35.924931 vero: 34.788974
```

**stderr** — [file TXT](streams/002_demo_energy_regression.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 003 · demo_examples

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "examples.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_demo_examples.stdout.txt)

```text
prima_riga_test: {"id": 180, "X": [31.96742015358659, 1.0, 3.0], "vero": 34.78897358564871, "previsto": 35.924931149734974, "baseline": 29.73755440685898}
temperature_simmetriche: [[10.0, 1.0, 12.0], [10.0, 1.0, 12.0]]
metriche_manuali: {'mae': 1.0, 'rmse': 1.2909944487358056}
senza_rumore: {"intercetta": 18.000000000000007, "coefficienti": [0.7999999999999992, 8.000000000000004, 0.0800000000000004], "metriche_test": {"mae": 6.217248937900877e-15, "rmse": 7.936161205069211e-15}}
esercizio: {'mae': 1.3333333333333333, 'rmse': 1.632993161855452}
```

**stderr** — [file TXT](streams/003_demo_examples.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
