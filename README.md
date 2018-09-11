# Towns in Malta
The following is a list of towns in Malta, together with their Latitude/Longitude coordinates. These were obtained using Google's geolocator service GoogleV3 together with geopy (python). The list of places itself is taken from [this wikipedia article](https://web.archive.org/web/20180911203230/https://en.wikipedia.org/wiki/List_of_towns_in_Malta), and is provided in the repository as `towns.txt`.

## Instructions
The two python modules provided, `json_output.py` and `md_output.py`, query the Google Maps API for Latitude/Longitude coordinates and respectively generate output files in JSON and markdown formats. A working Python 3 installation together with the [Geopy](https://geopy.readthedocs.io/) package are required. Additionally, a Google Maps API key will be necessary to generate the output files. You can obtain a key by starting a free trial [here](https://cloud.google.com/maps-platform/); then simply replace `ENTER_YOUR_KEY_HERE` in the python modules with your own key.

To generate the JSON file, navigate in a terminal to the pulled repository and simply write

```
python json_output.py
```

and similarly `python md_output.py` for the markdown output. The output files generated should match the contents of the `output.json` and `output.md` files provided.

Since some of the towns obtained are matched with incorrect coordinates, a truncated file `output_valid.json` is provided containing only valid results.


## Table of Towns
For convenience, the contents of `output.md` are presented below. Note that some of them are incorrect.

| *City or Town* | *What Google Maps API Recognised* | *Coordinates* |
|:--------------:|:---------------------------------:|:---------------:|
| Il-Belt Valletta, Malta | Valletta, Malta | 35.8989085, 14.5145528 |
| L-Imdina, Malta | Mdina, Malta | 35.888093, 14.4068357 |
| Il-Birgu, Malta | Birgu, Malta | 35.8879214, 14.522562 |
| L-Isla, Malta | Senglea, Malta | 35.8873041, 14.5167371 |
| Bormla, Malta | Cospicua, Malta | 35.8806753, 14.5218338 |
| Ħal Qormi, Malta | Qormi, Malta | 35.8764388, 14.4694186 |
| Ħaż-Żebbuġ, Malta | Haz-Zebbug, Malta | 35.8764648, 14.439084 |
| Ħaż-Żabbar, Malta | Ħaż-Żabbar, Malta | 35.8724715, 14.5451354 |
| Is-Siġġiewi, Malta | Siggiewi, Malta | 35.8463742, 14.4315746 |
| Iż-Żejtun, Malta | Żejtun, Malta | 35.8548714, 14.5363969 |
| Ħ'Attard, Malta | Attard, Malta | 35.8904967, 14.4199322 |
| Ħal Balzan, Malta | Balzan, Malta | 35.8957414, 14.4534065 |
| Birkirkara, Malta | Birkirkara, Malta | 35.8954706, 14.4665072 |
| Birżebbuġa, Malta | Birżebbuġa, Malta | 35.8135989, 14.5247463 |
| Ħad-Dingli, Malta | Ħad-Dingli, Malta | 35.8627309, 14.3850107 |
| Il-Fgura, Malta | Fgura, Malta | 35.8738269, 14.5232901 |
| Il-Furjana, Malta | Floriana, Malta | 35.8923386, 14.502904 |
| Il-Gudja, Malta | Gudja, Malta | 35.8469803, 14.502904 |
| Il-Gżira, Malta | Gzira, Malta | 35.905897, 14.4953338 |
| Ħal Għargħur, Malta | Ħal Għargħur, Malta | 35.9220569, 14.4563176 |
| Ħal Għaxaq, Malta | Ħal Għaxaq, Malta | 35.8440359, 14.516009 |
| Il-Ħamrun, Malta | Hamrun, Malta | 35.8861237, 14.4883442 |
| L-Iklin, Malta | Iklin, Malta | 35.9098774, 14.4577732 |
| Il-Kalkara, Malta | Kalkara, Malta | 35.8914242, 14.5320278 |
| Ħal Kirkop, Malta | Hal Kirkop, Malta | 35.8437862, 14.4854324 |
| Ħal Lija, Malta | Lija, Malta | 35.9013458, 14.440307 |
| Ħal Luqa, Malta | Luqa, Malta | 35.8582865, 14.4868883 |
| Il-Marsa, Malta | Marsa, Malta | 35.8735822, 14.492712 |
| Marsaskala, Malta | Marsaskala, Malta | 35.860364, 14.5567876 |
| Marsaxlokk, Malta | Marsaxlokk, Malta | 35.8411699, 14.5393097 |
| Il-Mellieħa, Malta | Mellieha, Malta | 35.9523529, 14.3500975 |
| L-Imġarr, Malta | Mgarr, Malta | 35.9189327, 14.3617343 |
| Il-Mosta, Malta | Mosta, Malta | 35.9141504, 14.4228427 |
| L-Imqabba, Malta | Mqabba, Malta | 35.8444143, 14.4694186 |
| L-Imsida, Malta | Msida, Malta | 35.8956388, 14.4868883 |
| In-Naxxar, Malta | Naxxar, Malta | 35.9317518, 14.4315746 |
| Raħal Ġdid, Malta | Paola, Malta | 35.8821077, 14.5101844 |
| Pembroke, Malta | Pembroke, Malta | 35.9290703, 14.4752416 |
| Tal-Pietà, Malta | Pieta, Malta | 35.8934116, 14.4941679 |
| Il-Qrendi, Malta | Qrendi, Malta | 35.8328488, 14.4548621 |
| Ir-Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Ħal Safi, Malta | Ħal Safi, Malta | 35.8362202, 14.492712 |
| San Ġiljan, Malta | St Julian's, Malta | 35.9181297, 14.4883442 |
| San Ġwann, Malta | San Gwann, Malta | 35.9077365, 14.4752416 |
| San Pawl il-Bahar, Malta | St Paul's Bay, Malta | 35.936017, 14.3966503 |
| Santa Luċija, Malta | Santa Luċija, Malta | 35.856142, 14.50436 |
| Santa Venera, Malta | Santa Venera, Malta | 35.8902201, 14.4766974 |
| Tas-Sliema, Malta | Sliema, Malta | 35.9110081, 14.502904 |
| Is-Swieqi, Malta | Swieqi, Malta | 35.9191182, 14.4694186 |
| Ta' Xbiex, Malta | Ta' Xbiex, Malta | 35.89914479999999, 14.4963519 |
| Ħal Tarxien, Malta | Tarxien, Malta | 35.8672552, 14.5116405 |
| Ix-Xgħajra, Malta | Xgħajra, Malta | 35.8868282, 14.5472391 |
| Iż-Żurrieq, Malta | Zurrieq, Malta | 35.8216306, 14.4810648 |
| L-Imtarfa, Malta | Imtarfa, Malta | 35.8895125, 14.3951953 |
| Baħar iċ-Ċagħaq, Malta | Baħar iċ-Ċagħaq, In-Naxxar, Malta | 35.9372576, 14.4519509 |
| Baħrija, Malta | Rabat, Malta | 35.8950089, 14.3465022 |
| Bubaqra, Malta | Bubaqra, Zurrieq, Malta | 35.8258138, 14.479609 |
| Burmarrad, Malta | Burmarrad, St Paul's Bay, Malta | 35.9350414, 14.4155666 |
| Fleur de Lys, Malta | 252 Triq Fleur - De - Lys, Birkirkara, Malta | 35.8920114, 14.4718674 |
| Gwardamanġa, Malta | Malta | 35.937496, 14.375416 |
| Ħal Farruġ, Malta | Ħal Farruġ, Luqa, Malta | 35.8612273, 14.4737858 |
| Madliena, Malta | Swieqi, Malta | 35.9308656, 14.4619582 |
| Paceville, Malta | Paceville, St Julian's, Malta | 35.9231053, 14.491256 |
| Kappara, Malta | Kappara, San Gwann, Malta | 35.9078199, 14.4854324 |
| San Pietru, Żabbar, Malta | San Pietru, Ħal Qormi, Malta | 35.8802094, 14.4720966 |
| Swatar, Malta | Is-Swatar, Msida, Malta | 35.8978656, 14.479609 |
| Tal-Virtù, Rabat, Malta | Tal-Virtù, Rabat, Malta | 35.8727915, 14.4010154 |
| L-Abatija, Imġarr, Malta | Mgarr, Malta | 35.9189327, 14.3617343 |
| Bulebel iż-Żgħir, Żabbar, Malta | Bulebel iż-Żgħir, Ħaż-Żabbar, Malta | 35.8686405, 14.5302074 |
| Albert Town, Marsa, Malta | Albert Town, Marsa, Malta | 35.8762916, 14.4978079 |
| L-Armier, Mellieħa, Malta | L-Armier, Mellieha, Malta | 35.9901703, 14.3624616 |
| Il-Ballut, Imġarr, Malta | Il-Ballut, Ħ'Attard, Malta | 35.8914993, 14.4318823 |
| Il-Balluta, San Ġiljan, Malta | Il-Balluta, St Julian's, Malta | 35.91417070000001, 14.49344 |
| Baqqari, Zurrieq, Malta | Zurrieq, Malta | 35.8216306, 14.4810648 |
| Belt-is-Sebħ, Floriana, Malta | Belt is-Sebħ, Floriana, Malta | 35.8954044, 14.5050881 |
| Bengħajsa, Birżebbuġa, Malta | Bengħajsa, Birżebbuġa, Malta | 35.8105709, 14.5276589 |
| Il-Beżbiżija, Mosta, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| Il-Bidni, Marsaskala, Malta | 35°51'38.8"N 14°33'23., Misrah l-4 ta' Settembru, Triq Il - Vitorja, L-Isla, Malta | 35.86077, 14.556514 |
| Il-Bidnija, Malta | Bidnija, Mosta, Malta | 35.9276614, 14.3995603 |
| Bieb ir-Ruwa, Rabat, Malta | Rabat, Malta | 35.889354, 14.367792 |
| Binġemma, Imġarr, Malta | Bingemma, L-Imġarr, Malta | 35.9172231, 14.3710455 |
| Birguma, Naxxar, Malta | Birguma, Naxxar, Malta | 35.9253936, 14.4454011 |
| Bir id-Deheb, Żejtun, Malta | Bir id-Deheb, Iż-Żejtun, Malta | 35.8502112, 14.5254745 |
| Il-Blata l-Bajda, Ħamrun, Malta | Il-Blata l-Bajda, Floriana, Malta | 35.887719, 14.4970799 |
| Il-Bokka taċ-Ċarcara, Imġarr, Malta | Il-Bokka taċ-Ċarċara, L-Imġarr, Malta | 35.9203957, 14.3551885 |
| Buġibba, San Pawl il-Baħar, Malta | Bugibba, St Paul's Bay, Malta | 35.9490844, 14.4097459 |
| Bulebel, Żejtun, Malta | Bulebel, Żejtun, Malta | 35.8631548, 14.5232901 |
| Buqana, Rabat, Malta | It Torri, L-Imtarfa, Malta | 35.8923834, 14.400465 |
| Il-Buskett, Ħad-Dingli, Malta | Il-Buskett, Ħad-Dingli, Malta | 35.8600378, 14.3864673 |
| Iċ-Ċanta, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Iċ-Ċens l-Iswed, Malta | Malta | 35.937496, 14.375416 |
| Iċ-Ċirkewwa, Malta | Cirkewwa, Mellieha, Malta | 35.9855354, 14.3348255 |
| Delimara, Malta | Delimara, Marsaxlokk, Malta | 35.8351932, 14.555331 |
| Id-Dwejra, Rabat, Malta | Id-Dwejra, Rabat, Malta | 35.9032078, 14.3922853 |
| Faqqanija, Malta | Malta | 35.937496, 14.375416 |
| Il-Fawwara, Siġġiewi, Malta | Il-Fawwara, Is-Siġġiewi, Malta | 35.8396947, 14.4097459 |
| Fomm ir-Riħ, Imġarr, Malta | Fomm ir-Riħ, Mgarr, Malta | 35.9088239, 14.3406432 |
| Fuq San Pawl, Bormla, Malta | San Pawl, Bormla, Malta | 35.8823309, 14.5192587 |
| Ġebel Ciantar, Siġġiewi, Malta | Ġebel Ciantar, Is-Siġġiewi, Malta | 35.8437836, 14.3981053 |
| Ġebel l-Abjad, Malta | IKL2902, Triq Hal-Gharghur, Iklin, Malta | 35.9095071, 14.4623938 |
| Ġebel San Martin, Żejtun, Malta | Ġebel San Martin, Iż-Żejtun, Malta | 35.86034739999999, 14.5298434 |
| Ġnejna Bay, Imġarr, Malta | Gnejna Bay, Malta | 35.9209421, 14.3424613 |
| Ġnien Borg, Malta | Malta | 35.937496, 14.375416 |
| Ġnien Fieres, Malta | Malta | 35.937496, 14.375416 |
| Ġnien San Pawl, Malta | Gnien, In-Naxxar, Malta | 35.9170822, 14.4459494 |
| Il-Girgenti, Siġġiewi, Malta | Il-Girgenti, Siggiewi, Malta | 35.8493082, 14.418477 |
| Il-Gwiedi, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| L-Għadira, Mellieħa, Malta | Għadira, Mellieha, Malta | 35.9671945, 14.3486429 |
| Għajn Astas, San Pawl il-Baħar, Malta | Għajn Tuffieħa, Mellieha, Malta | 35.9321743, 14.351552 |
| Għajn Dwieli, Malta | Għajn Dwieli, Raħal Ġdid, Malta | 35.87717070000001, 14.5123686 |
| Għajn il-Kbira, Malta | Il-Kbira, Ħad-Dingli, Malta | 35.8618046, 14.3842041 |
| Għajn Kajjet, Rabat, Malta | Triq Għajn Qajjet, Ir-Rabat RBT 4017, Malta | 35.8826924, 14.3912493 |
| Għajn Klieb, Rabat, Malta | Rabat, Malta | 35.8862686, 14.3842793 |
| Għajn Tajba, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Għajn Tuffieħa, Malta | Għajn Tuffieħa, Mellieha, Malta | 35.9321743, 14.351552 |
| L-Għallis, Naxxar, Malta | Tul Il-Kosta, Naxxar, Malta | 35.9533057, 14.4344687 |
| L-Għemieri, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Għar ix-Xiħ, Malta | Malta | 35.937496, 14.375416 |
| Għar Lapsi, Siġġiewi, Malta | Għar Lapsi, Malta | 35.827267, 14.4247528 |
| Għar Żerriegħa, Malta | Malta | 35.937496, 14.375416 |
| Ħaġar Qim, Qrendi, Malta | Triq Hagar Qim, Il-Qrendi QRD 2501, Malta | 35.8277061, 14.4417664 |
| Ħal Dmikki, Ħal Għaxaq, Malta | Ħal Dmikki, Ħal Għaxaq, Malta | 35.8472133, 14.5200136 |
| Ħal Dragu, Burmarrad, Malta | Burmarrad, St Paul's Bay, Malta | 35.9350414, 14.4155666 |
| Ħal Far, Malta | Ħal Far, Birżebbuġa, Malta | 35.818058, 14.5101844 |
| Ħal Tmiem, Żejtun, Malta | Ħal Tmiem, Iż-Żejtun, Malta | 35.8547511, 14.5454995 |
| Ħas-Saptan, Ħal Għaxaq, Malta | Ħas-Saptan, Ħal Għaxaq, Malta | 35.8371844, 14.5174652 |
| Ħlantun, Malta | Malta | 35.937496, 14.375416 |
| Il-Ħofra tar-Ritz, Malta | Il - Hofra, Ħaż-Żabbar, Malta | 35.8791898, 14.541541 |
| Il-Ħrieri, Żebbuġ, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| Il-Ħbula, Ħad-Dingli, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| Il-Ħfar, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| Il-Kalkara, Il-Baħrija, Malta | Kalkara, Malta | 35.8914242, 14.5320278 |
| Il-Katakombi, Rabat, Malta | Il-Katakombi, L-Imqabba, Malta | 35.8427018, 14.4682994 |
| Il-Ponta, Malta | 139B, Triq Spinola, San Ġiljan STJ 3208, Malta | 35.920122, 14.490886 |
| Kalafrana, Birżebbuġa, Malta | Kalafrana, Birżebbuġa, Malta | 35.8159914, 14.5378533 |
| Kordin, Paola, Malta | Kordin, Paola, Malta | 35.8809528, 14.5087283 |
| Il-Kunċizzjoni, Rabat, Malta | Il-Kunċizzjoni, Ħad-Dingli, Malta | 35.8609646, 14.3824445 |
| L-Aħrax, Mellieha, Malta | L-Aħrax, Mellieha, Malta | 35.9824816, 14.3544612 |
| L-Erba' Qaddisin, Ħal Qormi, Malta | l-, Erba' Qaddisin, Ħal Qormi, Malta | 35.8798853, 14.4820349 |
| Lippija, Imġarr, Malta | Ta' Lippija Tower, Mgarr, Malta | 35.9223878, 14.3460862 |
| Il-Lunzjata, Rabat, Malta | Rabat, Malta | 35.8766281, 14.39291 |
| Il-Magħtab, In-Naxxar, Malta | Il-Maghtab, Naxxar, Malta | 35.9308324, 14.4465703 |
| Il-Manikata, Il-Mellieħa, Malta | il-Manikata, Il-Mellieħa, Malta | 35.9407539, 14.3522793 |
| Manoel Island, Il-Gżira, Malta | Manoel Island, Gzira, Malta | 35.9037636, 14.502176 |
| Il-Marfa, Il-Mellieħa, Malta | Marfa, Mellieha, Malta | 35.9862086, 14.3457339 |
| Il-Marnisi, Birżebbuġa, Malta | Il-Marnisi, Marsaxlokk, Malta | 35.8460692, 14.5320278 |
| L-Imġiebaħ, Il-Mellieħa, Malta | L'Imgiebah, Malta | 35.9697222, 14.3858333 |
| Misraħ Kola, Ħ'Attard, Malta | Misrah Kola, Attard, Malta | 35.8909865, 14.4323023 |
| Il-Miżieb, Il-Mellieħa, Malta | Il-Miżieb, Malta | 35.9474685, 14.3573704 |
| L-Imrieħel, Birkirkara, Malta | L-Imrieħel, Birkirkara, Malta | 35.8886231, 14.4679629 |
| L-Imselliet, L-Imġarr, Malta | L-Imselliet, St Paul's Bay, Malta | 35.9161913, 14.3951953 |
| L-Imtaħleb, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| In-Nadur, Malta | Nadur, Malta | 36.0447019, 14.2919273 |
| In-Nigret, Iż-Żurrieq, Malta | In-Nigret, Zurrieq, Malta | 35.8232792, 14.4730579 |
| Il-Pwales, San Pawl il-Baħar, Malta | Il-Pwales, St Paul's Bay, Malta | 35.9440567, 14.3799187 |
| Il-Qajjenza, Birżebbuġa, Malta | Il-Qajjenza, Birżebbuġa, Malta | 35.8334815, 14.5312997 |
| Il-Qattara, Malta | Illinois, USA | 40.6331249, -89.3985283 |
| Il-Qawra, San Pawl il-Baħar, Malta | Il- Qawra, San Pawl il-Baħar, Malta | 35.9564031, 14.4232671 |
| Qerd in-Naħal, Malta | Malta | 35.937496, 14.375416 |
| Raba' Nemel, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Ras il-Wied, L-Imġarr, Malta | Ras il Pellegrin, ras il pellegrin, Malta | 35.9164572, 14.3375528 |
| Ricasoli, Il-Kalkara, Malta | Fort Rikasoli, St. Rocco Street, Il-Kalkara KKR 9062, Malta | 35.897264, 14.526449 |
| Is-Salina, In-Naxxar, Malta | Is-Salina, Naxxar, Malta | 35.9442845, 14.4272086 |
| San Ġwann t'Għuxa, Bormla, Malta | San Ġwann t'Għuxa, Cospicua, Malta | 35.8776094, 14.5196495 |
| San Lawrenz tal-Għolja, Is-Siġġiewi, Malta | Triq San Lawrenz ta' L-Gholja, Siggiewi, Malta | 35.8476606, 14.418244 |
| San Martin, San Pawl il-Baħar, Malta | San Martin, San Pawl il-Baħar, Malta | 35.93456219999999, 14.3805552 |
| San Niklaw, Il-Qrendi, Malta | San Niklaw Reservoir, Qrendi, Malta | 35.8372222, 14.4477778 |
| San Pawl tat-Tarġa, In-Naxxar, Malta | San Pawl tat-Tarġa, Naxxar, Malta | 35.9215281, 14.4388515 |
| Sant' Anton, Ħ'Attard, Malta | 24 G.Portelli, Ħ'Attard, Malta | 35.8964431, 14.4463108 |
| Santa Katerina, Rabat, Malta | Santa Katerina, Ir-Rabat, Malta | 35.8774602, 14.4025121 |
| Santa Margarita, Il-Mosta, Malta | 13 Mons.Mikiel Ang Mifsud, Il-Mosta, Malta | 35.9148579, 14.4288237 |
| Santa Marija Estate, Il-Mellieħa, Malta | Santa Maria Estate, Mellieha, Malta | 35.9620504, 14.3690078 |
| Is-Santi, L-Imġarr, Malta | Triq IS-Santi, Mgarr, Malta | 35.9109035, 14.3558964 |
| Is-Saqqajja, Rabat, Malta | Is-Saqqajja, Malta | 35.8830486, 14.403136 |
| Is-Sgħajtar, Il-Mosta, Malta | Is-Sgħajtar, Mosta, Malta | 35.9105269, 14.4333938 |
| L-Iskrivit, L-Imġarr, Malta | Mgarr, Malta | 35.9189327, 14.3617343 |
| Il-Bajja ta' San Ġorġ, San Ġiljan, Malta | St George's Bay, St Julian's, Malta | 35.9258157, 14.4878437 |
| Il-Bajja ta' San Tumas, Marsaskala, Malta | St Thomas Bay, Malta | 35.851859, 14.5662556 |
| Ta' Barkat, Ix-Xgħajra, Malta | Triq San Leonardu, Ix-Xgħajra, Malta | 35.881366, 14.5544279 |
| Ta' Brija, Is-Siġġiewi, Malta | Triq Ta' Bur Il-Kbir, Is-Siġġiewi, Malta | 35.8569413, 14.4205234 |
| Ta' Frajna, Malta | Malta | 35.937496, 14.375416 |
| Ta' Ganza, Iż-Żejtun, Malta | Ta' Ganza, Żejtun, Malta | 35.8555681, 14.5402199 |
| Ta' Giorni, San Giljan, Malta | Ta' Giorni, St Julian's, Malta | 35.9137311, 14.4861603 |
| Ta' Ġawhar, Malta | Ħal Safi, Malta | 35.8328938, 14.499633 |
| Ta' Għadajma, Malta | Malta | 35.937496, 14.375416 |
| Ta' Ħaramija, Malta | Malta | 35.937496, 14.375416 |
| Ta' Ħemsija, Malta | Hemsija, Ħ'Attard, Malta | 35.8899882, 14.414119 |
| Ta' Kandja, Is-Siġġiewi, Malta | Ta' Kandja, Is-Siġġiewi, Malta | 35.8477091, 14.4534065 |
| Ta' Lampat, Malta | Malta | 35.937496, 14.375416 |
| Ta' Landrijiet, Rabat, Malta | Wied il-busbies, Malta | 35.883762, 14.364315 |
| Ta' Lanza, Malta | Malta | 35.937496, 14.375416 |
| Ta' Laurenti, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Ta' Loretu, Il-Gudja, Malta | Gudja, Malta | 35.8416384, 14.5006496 |
| Ta' Mlit, Il-Mosta, Malta | Ta'Mlit, Il-Mosta, Malta | 35.9025391, 14.4337575 |
| Ta' Mrejnu, L-Imġarr, Malta | Ta' Mrejnu, Mgarr, Malta | 35.9279619, 14.3697351 |
| Ta' Newma, Malta | Malta | 35.937496, 14.375416 |
| Ta' Ngħajsa, Malta | Malta | 35.937496, 14.375416 |
| Ta' Paris, Birkirkara, Malta | Ta' Paris, Birkirkara, Malta | 35.8985374, 14.4686907 |
| Ta' Pascarella, Ħal Qormi, Malta | Qormi, Malta | 35.8753475, 14.466286 |
| Ta' Pennellu, Il-Mellieħa, Malta | Ta' Pennellu, Il-Mellieħa, Malta | 35.9556922, 14.361007 |
| Ta' Qali, Attard, Malta | Ta' Qali, Attard, Malta | 35.8919504, 14.4220925 |
| Ta' Rbazza, Malta | Malta | 35.937496, 14.375416 |
| Ta' Rużarju, Malta | Malta | 35.937496, 14.375416 |
| Ta' Tewma, Mgarr, Malta | Ta' Tewma, L-Imġarr, Malta | 35.9200658, 14.3606433 |
| Ta' Xurraf, Malta | Malta | 35.937496, 14.375416 |
| Ta' Żgamardi, Malta | Malta | 35.937496, 14.375416 |
| Ta' Żokkrija, Mosta, Malta | Ta' Żokkrija, Il-Mosta, Malta | 35.9127721, 14.4177494 |
| Ta' Żwejt, San Gwann, Malta | Ta' Żwejt, San Gwann, Malta | 35.9088285, 14.4690546 |
| Tal-Bebbux, Zurrieq, Malta | Tal-Bebbux, Zurrieq, Malta | 35.8325126, 14.4712382 |
| Tal-Blajjiet, Marsaskala, Malta | Marsaskala, Malta | 35.860364, 14.5567876 |
| Tal-Boxxla, Malta | Boxxla, San Pawl il-Baħar, Malta | 35.9480121, 14.4219753 |
| Tal-Bujjar, Marsaskala, Malta | Marsaskala, Malta | 35.860364, 14.5567876 |
| Tal-Ferħa, Gharghur, Malta | Ħal Għargħur, Malta | 35.9220569, 14.4563176 |
| Tal-Fuklar, Attard, Malta | Tal-Fuklar, Attard, Malta | 35.8948104, 14.4337576 |
| Tal-Ibraġ, Swieqi, Malta | Tal-Ibraġ, Is-Swieqi, Malta | 35.9204934, 14.4745137 |
| Tal-Għadir, Malta | Malta | 35.937496, 14.375416 |
| Tal-Għaqba, Malta | Malta | 35.937496, 14.375416 |
| Tal-Għolja, Siggiewi, Malta | Moghdija tal-Gholja, Siggiewi, Malta | 35.8501618, 14.4173491 |
| Tal-Ħamri, Malta | Malta | 35.937496, 14.375416 |
| Tal-Ħandaq, Qormi, Malta | Tal-Ħandaq, Qormi, Malta | 35.86958970000001, 14.4708743 |
| Tal-Ħawli, Birgu, Malta | Malta | 35.8815184, 14.5282097 |
| Tal-Kaccaturi, Malta | Malta | 35.937496, 14.375416 |
| Tal-Kanuni, Malta | Tal-Kanuni, Ir-Rabat, Malta | 35.8852745, 14.3902848 |
| Tal-Karwija, Malta | Ħal Safi, Malta | 35.8381333, 14.4963098 |
| Tal-Landier, Malta | Triq Prof Carmelo Coleiro, Ħal Qormi, Malta | 35.8693892, 14.4673871 |
| Tal-Laqnija, Malta | Malta | 35.937496, 14.375416 |
| Tal-Madliena Barra x-Xagħra, Malta | Xaghra, Malta | 36.050845, 14.267482 |
| Tal-Markiż, Malta | Tal-Markiż, Ir-Rabat, Malta | 35.8845071, 14.3897392 |
| Tal-Menħir Estate, Kirkop, Malta | Hal Kirkop, Malta | 35.8437862, 14.4854324 |
| Tal-Milord, Malta | Triq San Leonardu, Ix-Xgħajra, Malta | 35.8818444, 14.5455585 |
| Tal-Mirakli, Lija, Malta | Tal-Mirakli, Malta | 35.8988302, 14.4448611 |
| Tal-Palma, Mgarr, Malta | Mgarr, Malta | 35.9189327, 14.3617343 |
| Tal-Papa, Birzebbuga, Malta | Tal-Papa, Birżebbuġa, Malta | 35.8183605, 14.5240182 |
| Tal-Plier, Zabbar, Malta | Tal-Plier, Ħaż-Żabbar, Malta | 35.8722531, 14.5414943 |
| Tal-Providenza, Siggiewi, Malta | Siggiewi, Malta | 35.8374345, 14.4263691 |
| Tal-Qattus, Birkirkara, Malta | Tal-Qattus, Birkirkara, Malta | 35.8980021, 14.4730579 |
| Tal-Qroqq, Msida, Malta | Msida, Malta | 35.9034069, 14.4874342 |
| Tal-Wata, Malta | Wata, Il-Mosta, Malta | 35.9069406, 14.4222298 |
| Tar-Rabbat, Hamrun, Malta | Tar-Rabbat, Hamrun, Malta | 35.8832356, 14.4847045 |
| Tar-Ramel, Malta | Campsite 3 - Ahrax tar-Ramel, Triq Dahlet Ix-Xmajjar, Mellieha, Malta | 35.9886412, 14.3722809 |
| Tarġa Gap, Mosta, Malta | Targa Gap, Mosta, Malta | 35.9175, 14.4138889 |
| Tas-Salib, Malta | Sir Temi Zammit Ave, Ta' Xbiex, Malta | 35.899873, 14.498291 |
| Tas-Salib tal-Għolja, Siggiewi, Malta | Siggiewi, Malta | 35.8502319, 14.4166696 |
| Tas-Salvatur, Malta | Tas Salvatur, Żebbuġ, Malta | 36.0663889, 14.2541667 |
| Tas-Sirena, Malta | Triq Juan B. Azzopardo, Senglea (l'Isla), Malta | 35.8888018, 14.5172528 |
| Tat-Tabija, Malta | Malta | 35.937496, 14.375416 |
| Tat-Tilliera, Malta | Malta | 35.937496, 14.375416 |
| Upper Garden (Fuq il-Ġonna), Swieqi, Malta | Upper Barrakka Gardens, 292 Triq Sant' Orsla, Valletta, Malta | 35.8949004, 14.5121371 |
| Verdala, Bormla, Malta | Cospicua, Malta | 35.880599, 14.522358 |
| Wardija, San Pawl il-Bahar, Malta | Il-Wardija, St Paul's Bay, Malta | 35.9390386, 14.3937403 |
| Wied Fulija, Zurrieq, Malta | Wied Babu, Malta | 35.8238745, 14.4599618 |
| Wied Gerżuma, Malta | Malta | 35.937496, 14.375416 |
| Wied Ħazrun, Malta | Malta | 35.937496, 14.375416 |
| Wied Ħesri, Malta | Wied Hesri, Is-Siġġiewi, Malta | 35.8577528, 14.4341245 |
| Wied il-Bużbież, Malta | Wied Il- Ghasel, Malta | 35.9155058, 14.4250258 |
| Wied il-Kbir, Qormi, Malta | Wied il-Kbir, Triq Ħal Luqa, Qormi, Malta | 35.871603, 14.4767529 |
| Wied il-Lunzjata, Victoria, Malta | Ta Mulejja Lunzjata Mansions Il-Fontana - Gozo MT FNT, 1112, Il-Fontana, Malta | 36.0384877, 14.2355577 |
| Wied is-Sewda, Qormi, Malta | Qormi, Malta | 35.8764388, 14.4694186 |
| Wied iż-Żebbuġ, Malta | Triq Is-Sagħtrija, Iż-Żebbuġ, Malta | 36.0795327, 14.2296553 |
| Wied iż-Żiju, Marsaskala, Malta | Wied iz-Ziju, Marsaskala, Malta | 35.8611111, 14.5508333 |
| Wied iż-Żurrieq, Qrendi, Malta | Wied Iż-Żurrieq, Il-Qrendi, Malta | 35.8206338, 14.4537704 |
| Wied Rini, Rabat, Malta | Il Wied, Ir-Rabat Għawdex, Malta | 36.0444992, 14.2362911 |
| Wied ta' Baqqiegħa, Malta | Baqqiegha & Wied Ta', Ħaż-Żebbuġ, Malta | 35.86737919999999, 14.4458384 |
| Wied ta' Ħal Mula, Haz-Zebbug, Malta | Haz-Zebbug, Malta | 35.8712346, 14.4469839 |
| Wied ta' San Martin, Malta | S.Martin, Ir-Rabat RBT 1300, Malta | 35.8835434, 14.399023 |
| Wied ta' Sant' Antnin, Malta | Wied Ta', Ħaż-Żebbuġ, Malta | 35.8676214, 14.4444914 |
| Wied tal-Blata, Malta | Tal-Blata, Qala, Malta | 36.0280556, 14.3266667 |
| Wied tal-Ħandaq, Qormi, Malta | Tal-Ħandaq, Qormi, Malta | 35.86958970000001, 14.4708743 |
| Wied tal-Isperanza, Mosta, Malta | 4 Triq il-Kapella ta' l-Isperanza, Il-Mosta, Malta | 35.909606, 14.4192728 |
| Wied tal-Isqof, Rabat, Malta | Wied Ta'l- Isperanza, Il-Mosta, Malta | 35.9079147, 14.4153848 |
| Wied tal-Qlejgħa (Chadwick Lakes), Mosta, Malta | Chadwick Lakes, Rabat, Malta | 35.8973387, 14.3964692 |
| Wied tat-Troll, Malta | Wied Babu, Malta | 35.8238745, 14.4599618 |
| Wied Xkora, Malta | Malta | 35.937496, 14.375416 |
| Xagħra Ħurija, Malta | Xaghra, Malta | 36.050845, 14.267482 |
| Xagħra tal-Isqof, Rabat, Malta | Rabat, Malta | 35.8854994, 14.373372 |
| Xemxija, San Pawl il-Bahar, Malta | Xemxija, St Paul's Bay, Malta | 35.950551, 14.380172 |
| Xifer il-Kief, Mgarr, Malta | Xifer, Il-Mellieħa, Malta | 35.9401295, 14.3544182 |
| Xrob l-Għagin, Marsaxlokk, Malta | Xrobb L-Ghagin Nature Park And Sustainable Development Centre, Marsaxlokk MXK 4080, Malta | 35.8431433, 14.5676786 |
| Xwieki, Gharghur, Malta | Ix-Xwieki, Ħal Għargħur, Malta | 35.9189908, 14.4541343 |
| Żebbiegħ, Mgarr, Malta | Żebbiegħ, Mgarr, Malta | 35.9200536, 14.3799187 |
| Żonqor, Marsaskala, Malta | Żonqor, Malta | 35.867085, 14.573266 |
| Ir-Rabat, Gozo | Victoria, Malta | 36.0426891, 14.2425011 |
| Il-Fontana, Gozo | Fontana, Malta | 36.0369053, 14.2352339 |
| Għajnsielem, Gozo | Ghajnsielem, Malta | 36.02479659999999, 14.2802961 |
| L-Għarb, Gozo | Gharb, Malta | 36.068909, 14.2018098 |
| L-Għasri, Gozo | Għasri, Malta | 36.0668075, 14.2192475 |
| Ta' Kerċem, Gozo | Kerċem, Malta | 36.04479389999999, 14.2250605 |
| Il-Munxar, Gozo | Munxar, Malta | 36.0288058, 14.2250605 |
| In-Nadur, Gozo | Nadur, Malta | 36.0447019, 14.2919273 |
| Il-Qala, Gozo | Qala, Malta | 36.0388628, 14.318101 |
| San Lawrenz, Gozo | San Lawrenz, Malta | 36.0482955, 14.1959978 |
| Ta' Sannat, Gozo | Sannat, Malta | 36.0192643, 14.2599437 |
| Ix-Xagħra, Gozo | Xaghra, Malta | 36.050845, 14.267482 |
| Ix-Xewkija, Gozo | Ix-Xewkija, Malta | 36.0299236, 14.2599437 |
| Iż-Żebbuġ, Gozo | Żebbuġ, Malta | 36.0716403, 14.245408 |
| Xlendi, Gozo | Xlendi, Malta | 36.031265, 14.217432 |
| Ix-Xlendi, Gozo | Xlendi, Malta | 36.031265, 14.217432 |
| Marsalforn, Gozo | Marsalforn, Żebbuġ, Malta | 36.0717421, 14.2555828 |
| Santa Luċija, Gozo | Santa Lucija, Malta | 36.04167330000001, 14.2177943 |
| Birbuba, L-Għarb, Gozo | Birbuba, Gharb, Malta | 36.0643347, 14.2010833 |
| Borġ Għarib, Għajnsielem, Gozo | Borġ Għarib, Ghajnsielem, Malta | 36.0311556, 14.2882925 |
| Iċ-Ċittadella, Victoria, Gozo | It-Telgħa tal-Belt, Ir-Rabat Għawdex, Malta | 36.0465151, 14.2397758 |
| Daħlet Qorrot, Il-Qala, Gozo | Dahlet Qorrot Bay, Qala, Malta | 36.0496827, 14.3163866 |
| Fort Chambray, Għajnsielem, Gozo | Ghajnsielem, Malta | 36.0209908, 14.2916515 |
| Għajn Ħosna, Ix-Xagħra, Gozo | Xagħra, Malta | 36.050368, 14.277402 |
| Għajn Lukin, Ix-Xagħra, Gozo | Ghajn Lukin, Ix-Xagħra, Malta | 36.0473977, 14.2565444 |
| Għar ix-Xiħ, Għajnsielem, Gozo | Ghajnsielem, Malta | 36.02479659999999, 14.2802961 |
| Ħondoq ir-Rummien, Il-Qala, Gozo | Hondoq Bay, Qala, Malta | 36.02778900000001, 14.3242816 |
| Id-Dwejra, San Lawrenz, Gozo | San Lawrenz, Malta | 36.0535258, 14.1882246 |
| Il-Qbajjar, Marsalforn, Gozo | Triq Ix-Xwejni, Iż-Żebbuġ, Malta | 36.0770624, 14.2515702 |
| Il-Qortin, In-Nadur, Gozo | Il-Qortin Isopo, Nadur, Malta | 36.0480556, 14.3022222 |
| Ix-Xwejni, Marsalforn, Gozo | Triq Ix-Xwejni, Iż-Żebbuġ, Malta | 36.0768335, 14.2516001 |
| Kemmuna, Għajnsielem, Gozo | Comino, Malta | 36.0100996, 14.3355527 |
| Kemmunett, Għajnsielem, Gozo | Cominotto‎, Malta | 36.01366420000001, 14.3199188 |
| L-Imġarr, Għajnsielem, Gozo | Mgarr, Malta | 36.0245932, 14.2984703 |
| Mġarr ix-Xini, Ta' Sannat, Gozo | Mgarr ix-Xini, Għajnsielem, Malta | 36.0204489, 14.2713234 |
| Ir-Ramla l-Ħamra, Ix-Xagħra, Gozo | Ramla Beach, Malta | 36.0614643, 14.2841125 |
| San Blas, In-Nadur, Gozo | San Blas Bay, Malta | 36.0572011, 14.3007422 |
| Santu Pietru, L-Għarb, Gozo | Santu Pietru, Gharb, Malta | 36.0605137, 14.1996303 |
| Ta' Bin Ġemma, In-Nadur, Gozo | Triq Wied Bingemma, Nadur NDR 1900, Malta | 36.0433474, 14.2925957 |
| Ta' Ċenċ, Ta' Sannat, Gozo | Ta' Ċenċ, Sannat, Malta | 36.0218263, 14.2497686 |
| Ta' Cordina, Għajnsielem, Gozo | Triq Ta' Cordina, Għajnsielem, Malta | 36.0250759, 14.2855901 |
| Ta' Dbieġi, L-Għarb, Gozo | Triq Santu Pietru 50 L-Għarb MT GRB, 1507, Gharb, Malta | 36.0602078, 14.2006519 |
| Ta' Għammar, L-Għasri, Gozo | Ta' Għammar, Għasri, Malta | 36.0668075, 14.2192475 |
| Ta' Ħamet, Ix-Xagħra, Gozo | Xagħra, Malta | 36.0581741, 14.2686658 |
| Ta' Kuxxina, In-Nadur, Gozo | San Gakbu, Nadur NDR 8323, Malta | 36.038714, 14.2979846 |
| Ta' Nazzarenu, Ix-Xagħra, Gozo | Triq Gnien Xibla, Xaghra, gozo, Malta | 36.051015, 14.27478 |
| Ta' Pinu, L-Għarb, Gozo | Gharb, Malta | 36.0619707, 14.2148387 |
| Ta' Seguna, Ta' Sannat, Gozo | Sannat, Malta | 36.0192643, 14.2599437 |
| Ta' Xħajma, In-Nadur, Gozo | San Gakbu, Nadur NDR 8323, Malta | 36.038714, 14.2979846 |
| Taċ-Ċawla, Victoria, Malta, Gozo | Taċ-Ċawla, Victoria, Malta | 36.0364927, 14.241411 |
| Tal-Barmil, Ix-Xewkija, Gozo | Ix-Xewkija, Malta | 36.033208, 14.2663639 |
| Tal-Ħniena, Ix-Xewkija, Gozo | Triq San Bert, Xewkija, Malta | 36.0325421, 14.2680323 |
| Tal-Ibraġ, Victoria, Gozo | Triq Bieb l-Imdina, Ir-Rabat Għawdex, Malta | 36.045885, 14.2394614 |
| Tal-Kaċċaturi, Ix-Xagħra, Gozo | Xaghra, Malta | 36.050845, 14.267482 |
| Wied il-Għasri, L-Għasri, Gozo | Wied Il-Għasri, Malta | 36.0787685, 14.2284213 |
| Wied il-Lunzjata, Il-Fontana, Gozo | Ta Mulejja Lunzjata Mansions Il-Fontana - Gozo MT FNT, 1112, Il-Fontana, Malta | 36.0384877, 14.2355577 |
| Wied il-Mielaħ, L-Għarb, Gozo | Gharb, Malta | 36.0790243, 14.2129773 |
| Wied tal-Blata, Il-Qala, Gozo | Tal-Blata, Qala, Malta | 36.0280556, 14.3266667 |
| Xatt l-Aħmar, Għajnsielem, Gozo | Xatt l-Ahmar, Ghajnsielem, Malta | 36.0192779, 14.2901099 |
