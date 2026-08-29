# Script 24: Online Travel Agency (GoZayaan / ShareTrip / Flyfarint)

---

## Scenario ১ঃ Dhaka-Bangkok flight ২৮,০০০ টাকায় book করা হয়েছে কিন্তু confirmation email এ ৩২,০০০ টাকা দেখাচ্ছে

> Customer GoZayaan app এ Dhaka-Bangkok একটি flight ২৮,০০০ টাকায় book করেছেন এবং সেই amount এ payment করেছেন। কিন্তু confirmation email এ দেখাচ্ছে ৩২,০০০ টাকা charge হয়েছে। তিনি ক্ষুব্ধ হয়ে helpline এ call করেছেন।

**১. Agent:** শুভ সকাল, 'GoZayaan' customer support থেকে আমি Nabil বলছি। কীভাবে assist করতে পারি?

**২. Customer:** নাবিল সাহেব, আপনাদের platform এ একটা বড় সমস্যা হয়েছে। আমি Dhaka-Bangkok flight এ ২৮,০০০ টাকা দেখে book করলাম, payment ও করলাম। এখন email এ দেখাচ্ছে ৩২,০০০ টাকা!

**৩. Agent:** Sir, এটা দেখে সত্যিই concerned হলাম। Kindly আপনার booking reference number টা বলবেন?

**৪. Customer:** Booking ID হচ্ছে GZ-887654। ৪,০০০ টাকা extra charge হয়েছে, কোনো explanation ছাড়া! এটা কি জোচ্চুরি না?

**৫. Agent:** Sir, আমি আপনার booking টি এখনই pull up করছি। (Pause) Sir, আমি দেখতে পাচ্ছি। আপনার base fare ছিল ২৮,০০০ টাকা, কিন্তু তার সাথে যোগ হয়েছে platform convenience fee ২,০০০ টাকা এবং airport development levy ২,০০০ টাকা।

**৬. Customer:** এই fees গুলো booking এর সময় কেন দেখায়নি? আমি যদি আগে জানতাম এত extra charge আছে, হয়তো আলাদা কোথাও থেকে করতাম।

**৭. Agent:** Sir, আপনার point টা সম্পূর্ণ valid। আমাদের payment page এ এই breakdown টা clearly visible থাকার কথা ছিল। আপনি কি payment এর আগে final summary screen দেখেছিলেন?

**৮. Customer:** আমি final page এ একটা total amount দেখেছিলাম, তবে এত detail এ breakdown দেখিনি। App এ তো সব এত ছোট ছোট লেখায় থাকে!

**৯. Agent:** Sir, আমি honestly স্বীকার করছি, আমাদের checkout flow এ breakdown টা আরও prominently দেখানো উচিত ছিল। এই UI issue এর জন্য আমি sincerely apologize করছি।

**১০. Customer:** Apology তে তো কাজ হবে না। আমি এই extra ৪,০০০ টাকা refund চাই।

**১১. Agent:** Sir, আমি আপনার concern টা বুঝতে পারছি। কিন্তু platform convenience fee এবং airport levy গুলো third party charges, যা আমরা collect করে সংশ্লিষ্ট authority এ pass করি। এগুলো refundable না।

**১২. Customer:** কিন্তু আমাকে আগে জানানো হয়নি! এটা কি consumer rights এর লঙ্ঘন না?

**১৩. Agent:** Sir, আমি আপনার frustration টা সম্পূর্ণ বুঝতে পারছি। আমি এই issue টি আমাদের Product team এ escalate করছি যেন checkout এ fee breakdown আরও clearly display হয়।

**১৪. Customer:** Escalate করলে আমার কী লাভ? আমার পকেট থেকে তো ৪,০০০ টাকা গেছে।

**১৫. Agent:** Sir, refund না হলেও আমি আপনার account এ ২,০০০ টাকার GoZayaan travel credit add করতে পারি। এটা আপনার next booking এ use করতে পারবেন।

**১৬. Customer:** Travel credit? আমি কি cash refund পেতে পারি না?

**১৭. Agent:** Sir, আমি honestly বলছি, এই charges গুলো genuinely third-party, তাই cash refund technically possible না। তবে ২,০০০ টাকার travel credit টা আপনার পরবর্তী trip এ real value দেবে।

**১৮. Customer:** ঠিক আছে। ২,০০০ টাকা travel credit হলেও accept করছি। কিন্তু আপনাদের checkout page fix করুন।

**১৯. Agent:** Sir, absolutely। আমি আপনার feedback টি user experience improvement request হিসেবে log করছি। Travel credit টা আজকেই আপনার account এ visible হবে।

**২০. Customer:** ঠিক আছে নাবিল সাহেব। Bangkok trip এর জন্য অন্য কোনো extra charge হবে না তো?

**২১. Agent:** Sir, confirmation email এ দেখানো ৩২,০০০ টাকাই final amount। এর বাইরে GoZayaan এর কোনো additional charge নেই। Airport এ নিজস্ব taxes আলাদা হতে পারে তবে সেটা airline এর বিষয়।

**২২. Customer:** ঠিক আছে, বুঝলাম। Travel credit দিয়ে next trip এ কাজে লাগাবো।

**২৩. Agent:** Enjoy your Bangkok trip sir! 'GoZayaan' এ call করার জন্য ধন্যবাদ। ভালো থাকবেন।

---

## Scenario ২ঃ Airline flight cancel করেছে — GoZayaan বলছে refund ৪৫ দিনে হবে, কিন্তু customer এর এখনই টাকা দরকার rebooking এর জন্য

> Customer এর Biman Bangladesh Airlines এর Dhaka-Kolkata flight airline কর্তৃক cancel হয়েছে। GoZayaan বলছে airline এর policy অনুযায়ী refund হতে ৪৫ দিন লাগবে। কিন্তু customer কে দ্রুত alternative flight book করতে হবে, তাই অবিলম্বে refund চাইছেন।

**১. Agent:** শুভ দুপুর, 'GoZayaan' support থেকে আমি Tisha বলছি। কীভাবে assist করতে পারি?

**২. Customer:** তিশা আপু, আমি অনেক বড় সমস্যায় পড়েছি। Biman আমার Kolkata flight cancel করে দিয়েছে। আমার ওখানে জরুরি medical appointment আছে।

**৩. Agent:** Mam, এটা সত্যিই একটি stressful situation, বিশেষত যখন medical appointment জড়িত। আমি এখনই আপনার booking টা check করছি। Booking reference টা বলবেন?

**৪. Customer:** GZ-445566। আমার flight ছিল কাল সকালে। Biman আজ সকালে SMS দিয়ে জানিয়েছে flight cancelled।

**৫. Agent:** Mam, আমি দেখছি। হ্যাঁ, Biman DA-405 flight টি airline side থেকে operational reason এ cancel করা হয়েছে। আপনার ticket এর total amount ছিল ১৮,৫০০ টাকা।

**৬. Customer:** আমি এই ১৮,৫০০ টাকা এখনই ফেরত চাই। আমাকে তো alternative flight বুক করতে হবে, সেটার জন্যও টাকা লাগবে।

**৭. Agent:** Mam, আপনার কথাটা আমি পুরোপুরি বুঝতে পারছি। Airline cancel এর ক্ষেত্রে আমরা ১০০% refund এর guarantee দিচ্ছি। কিন্তু airline থেকে টাকা আসতে ৩০-৪৫ business day সময় লাগে।

**৮. Customer:** ৪৫ দিন? কিন্তু আমার এখনই টাকা দরকার! আমার Kolkata তে specialist এর appointment মিস হয়ে গেলে পরের appointment নিতে ৩ মাস লাগবে।

**৯. Agent:** Mam, এই urgency টা আমি সম্পূর্ণ respect করছি। আপনার situation টা medical emergency category তে পড়ে। আমি একটা alternative solution নিয়ে কথা বলতে চাই।

**১০. Customer:** কী solution?

**১১. Agent:** Mam, GoZayaan এর 'Emergency Rebooking Assist' program এর আওতায়, airline cancel হলে আমরা customer কে পরবর্তী available flight এ priority rebooking অফার করি এবং refund এর টাকা directly new booking এ adjust করি।

**১২. Customer:** মানে নতুন ticket কাটতে হবে কিন্তু আমাকে আবার pay করতে হবে না? টাকাটা directly apply হবে?

**১৩. Agent:** Mam, exactly। আপনার ১৮,৫০০ টাকার credit টা আজকেই আপনার account এ pending credit হিসেবে show করবে এবং সেটা দিয়েই new ticket book করতে পারবেন।

**১৪. Customer:** আচ্ছা, কিন্তু alternative flight এর price যদি বেশি হয়?

**১৫. Agent:** Mam, যদি new flight এর price বেশি হয় তাহলে শুধু difference amount টা আপনাকে pay করতে হবে। আর যদি কম হয়, বাকি credit পরবর্তী booking এ use করতে পারবেন।

**১৬. Customer:** এটা তো reasonable। কাল Kolkata র জন্য কোনো alternative flight আছে কি?

**১৭. Agent:** Mam, আমি check করছি। (Pause) IndiGo কাল সকাল ৯:৩০ AM এ একটা flight আছে, মূল্য ২২,০০০ টাকা। আর US-Bangla র ১১:৪৫ AM এ আছে, ১৯,৮০০ টাকায়।

**১৮. Customer:** US-Bangla র flight টা কাছাকাছি price। সেটা কি book করা possible?

**১৯. Agent:** Mam, absolutely। আমি এখনই আপনার existing credit দিয়ে US-Bangla flight টা book করে দিচ্ছি। Difference টা হবে মাত্র ১,৩০০ টাকা, যা আপনি এখন pay করলেই হবে।

**২০. Customer:** ঠিক আছে, ১,৩০০ টাকা বিকাশ এ করে দিচ্ছি। আমার appointment যেন miss না হয়।

**২১. Agent:** Mam, payment receive হওয়ার সাথে সাথেই confirmation email পাঠিয়ে দিচ্ছি। আর Biman এর original refund টা ৪৫ দিনের মধ্যে আপনার original payment method এ ফেরত যাবে।

**২২. Customer:** ঠিক আছে তিশা আপু। আপনি অনেক helpful ছিলেন, thanks।

**২৩. Agent:** Mam, আপনার Kolkata যাত্রা সফল হোক এবং treatment ও ভালোভাবে হোক। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৩ঃ Cox's Bazar এর hotel app এ ৫ star দেখাচ্ছিল কিন্তু বাস্তবে room টা photo এর মতো না — relocation চাইছেন

> Customer GoZayaan থেকে Cox's Bazar এর একটি sea-facing hotel book করেছিলেন, যেটাকে app এ "5-star deluxe" দেখানো হয়েছে। কিন্তু hotel এ এসে দেখেন room টা app এর photo থেকে সম্পূর্ণ আলাদা, sea view নেই এবং room পুরনো ও damp। তিনি রাগান্বিত হয়ে GoZayaan এ call করেছেন।

**১. Agent:** শুভ বিকাল, 'GoZayaan' support থেকে আমি Hasan বলছি। কীভাবে assist করতে পারি?

**২. Customer:** হাসান সাহেব, আমি এখন Cox's Bazar এ আছি। আপনাদের app থেকে যে hotel book করেছিলাম, সেটা দেখে মাথা ঘুরছে!

**৩. Agent:** Sir, কী হয়েছে? Kindly বিস্তারিত বলুন। Booking reference number টাও বলবেন।

**৪. Customer:** Booking ID GZ-334455। আমি 'Pearl Continental Sea View' বুক করেছিলাম। App এ ছিল beautifully decorated sea-facing room। এখানে এসে দেখি ছোট একটা room, দেওয়াল এ ছত্রাক, sea view তো দূরের কথা, জানালা দিয়ে পাশের building দেখা যাচ্ছে!

**৫. Agent:** Sir, এটা শুনে আমি সত্যিই shocked। আমি এখনই booking details এবং hotel এর listed amenities টা pull up করছি।

**৬. Customer:** আমি এখানে travel করতে এসেছি আমার wife এর সাথে। এটা আমাদের anniversary trip। এই room এ থাকা কি সম্ভব?

**৭. Agent:** Sir, আমি genuinely দুঃখিত। Anniversary trip এ এমন experience হওয়া সম্পূর্ণ unacceptable। আমি hotel এর listed description চেক করছি। (Pause) Sir, booking এ clearly "sea-facing deluxe room" এবং "renovated interior" উল্লেখ আছে।

**৮. Customer:** তাহলে তারা কেন আমাকে এই room এ দিল? Hotel management কে বললাম, তারা বলছে "এটাই আমাদের standard room।"

**৯. Agent:** Sir, hotel যদি listed description অনুযায়ী room না দেয়, এটা contract breach। আমি এখনই hotel এর reservation manager কে call করছি।

**১০. Customer:** আপনারা call করেন, আমি এখানে দাঁড়িয়ে আছি। কিন্তু আমার এখনই solution দরকার।

**১১. Agent:** Sir, অবশ্যই। আমি এখন hotel এ call করছি, আপনি কি একটু hold এ থাকবেন?

**১২. Customer:** থাকছি।

**১৩. Agent:** (Pause) Sir, আমি hotel এর duty manager এর সাথে কথা বললাম। তারা বলছেন সব sea-facing room এখন occupied। তবে তারা আগামীকাল সকালে upgrade করে দিতে পারবেন।

**১৪. Customer:** আগামীকাল? আজকের রাতটা কোথায় কাটাবো? এই damp room এ?

**১৫. Agent:** Sir, এটা একদমই acceptable না। আমি GoZayaan এর পক্ষ থেকে আপনার জন্য পাশের 'Ocean Paradise Hotel' এ একটা sea-facing room এর availability check করছি।

**১৬. Customer:** পাশের hotel এ shift করা possible হলে ভালো হয়। কিন্তু extra charge কি আমাকে দিতে হবে?

**১৭. Agent:** Sir, এটা আমাদের listed hotel এর failure। GoZayaan সম্পূর্ণ দায়িত্ব নিচ্ছে। যদি alternative hotel এর rate বেশি হয়, সেই difference GoZayaan bear করবে।

**১৮. Customer:** তাহলে তো ভালোই হয়। Ocean Paradise এ কি room আছে?

**১৯. Agent:** Sir, (Pause) হ্যাঁ, একটা sea-facing room available আছে, আজ রাতের জন্য। Price difference হবে ১,২০০ টাকা যা GoZayaan cover করবে। আমি এখনই book করে দিচ্ছি।

**২০. Customer:** Perfect। Confirmation টা WhatsApp এ পাঠিয়ে দিন, আমি এখনই shift করছি।

**২১. Agent:** Sir, confirmation পাঠিয়ে দিচ্ছি। আর original hotel এর বিরুদ্ধে আমরা formal complaint file করব এবং listing verify না হওয়া পর্যন্ত তাদের GoZayaan এ suspend করব।

**২২. Customer:** ধন্যবাদ হাসান সাহেব। আপনারা দ্রুত solution দিয়েছেন, এটা appreciate করছি।

**২৩. Agent:** Sir, আপনার anniversary trip টা সুন্দর হোক। 'GoZayaan' এর পক্ষ থেকে আবারো ক্ষমা চাইছি। ভালো থাকবেন।

---

## Scenario ৪ঃ Family visa application জমা দেওয়ার ২ সপ্তাহ পরেও কোনো update নেই — ৩ দিন পরে embassy appointment

> Customer GoZayaan এর visa assistance service এর মাধ্যমে family সহ Malaysia ভ্রমণের জন্য visa documents ২ সপ্তাহ আগে submit করেছেন। এখনো কোনো update পাননি। ৩ দিন পরে embassy appointment এর জন্য আতঙ্কিত হয়ে call করেছেন।

**১. Agent:** শুভ সকাল, 'GoZayaan' visa support থেকে আমি Nabil বলছি। কীভাবে assist করতে পারি?

**২. Customer:** নাবিল সাহেব, আমি Malaysia visa এর জন্য ২ সপ্তাহ আগে documents দিয়েছিলাম। কোনো update নেই। ৩ দিন পরে embassy appointment!

**৩. Agent:** Sir, আমি বুঝতে পারছি এটা কতটা stressful। Kindly আপনার visa application reference number টা বলবেন?

**৪. Customer:** Reference number VA-112233। আমার family তে আমি, আমার wife, আর দুই বাচ্চা। সবার documents দিয়েছিলাম।

**৫. Agent:** Sir, আমি system এ application টা check করছি। (Pause) আমি দেখছি application টা 2 সপ্তাহ আগে received হয়েছে। তবে এটা এখনো 'Document Verification' stage এ আছে।

**৬. Customer:** Document Verification এ ২ সপ্তাহ লাগে? আপনাদের website এ তো লেখা আছে processing ৫-৭ দিন!

**৭. Agent:** Sir, আপনি সম্পূর্ণ ঠিক বলেছেন, আমাদের committed turnaround time ৭ দিন। এই delay টা অগ্রহণযোগ্য। আমি immediately এই issue টা our visa coordinator কে escalate করছি।

**৮. Customer:** Escalate করলে কি ৩ দিনের মধ্যে visa পাবো? Embassy appointment miss করা যাবে না।

**৯. Agent:** Sir, embassy appointment যদি miss হয়, পরের slot পেতে আরও সপ্তাহ লাগতে পারে। আমি আমাদের senior visa manager কে এখনই call করছি। একটু hold এ থাকবেন?

**১০. Customer:** থাকছি।

**১১. Agent:** (Pause) Sir, আমি senior manager এর সাথে কথা বললাম। তিনি আপনার application টা personally handle করবেন এবং আজকের মধ্যেই document review complete করবেন।

**১২. Customer:** আজকের মধ্যে complete হলে কি embassy appointment এর আগে visa পাবো?

**১৩. Agent:** Sir, document verification আজ শেষ হলে আগামীকাল embassy submission হবে। Embassy appointment ৩ দিন পরে হওয়ায় timeline টা tight কিন্তু possible।

**১৪. Customer:** Possible মানে কি নিশ্চিত না? আমার family নিয়ে plan করা আছে।

**১৫. Agent:** Sir, আমি guarantee দিতে পারবো না কারণ final approval embassy এর হাতে। তবে আমরা সর্বোচ্চ priority দিয়ে আপনার application process করবো।

**১৬. Customer:** যদি visa না হয়, তাহলে GoZayaan কি আমার flight ticket refund দেবে?

**১৭. Agent:** Sir, GoZayaan এর visa service এর terms অনুযায়ী, visa rejection বা delay এর কারণে flight refund করা হয়। তবে airline এর cancellation policy applicable হবে।

**১৮. Customer:** Airline এর policy কী? এটা কি full refund হবে?

**১৯. Agent:** Sir, ticket টা যদি refundable হয়ে থাকে তাহলে full refund। আমি এখনই আপনার ticket টা check করছি। (Pause) Sir, আপনার ticket টা 'Flexible Refundable' category তে আছে। Visa issue হলে 100% refund পাবেন।

**২০. Customer:** সেটা জেনে একটু নিশ্চিন্ত হলাম। কিন্তু আমি চাই যেন visa হোক, refund না।

**২১. Agent:** Sir, আমিও তাই চাই। আমাদের visa team আজ থেকেই সর্বোচ্চ priority তে কাজ করবে। সন্ধ্যার মধ্যে আপনাকে update দেওয়া হবে।

**২২. Customer:** ঠিক আছে নাবিল সাহেব। সন্ধ্যার update এর জন্য wait করছি।

**২৩. Agent:** অবশ্যই sir। আপনার Malaysia trip সফল হোক। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৫ঃ Domestic flight ticket এ passenger এর last name এ typo হয়েছে — name correction করতে চাইছেন

> Customer GoZayaan এ Dhaka-Chittagong domestic flight book করেছেন। কিন্তু ticket এ last name "Ahmed" এর বদলে "Ahemed" হয়ে গেছে। Flight আগামীকাল, তিনি এখন correction করাতে চাইছেন।

**১. Agent:** শুভ সন্ধ্যা, 'GoZayaan' support থেকে আমি Fahim বলছি। কীভাবে assist করতে পারি?

**২. Customer:** ফাহিম সাহেব, আমার কাল Dhaka-Chittagong flight আছে। টিকিট check করতে গিয়ে দেখলাম আমার last name ভুল হয়েছে।

**৩. Agent:** Sir, এটা অবশ্যই ঠিক করা দরকার। Kindly booking ID এবং কী ভুল হয়েছে সেটা বলবেন।

**৪. Customer:** Booking ID GZ-998877। Last name "Ahmed" হওয়ার কথা, কিন্তু ticket এ "Ahemed" হয়েছে। মাঝখানে একটা "e" extra ঢুকে গেছে।

**৫. Agent:** Sir, এটা একটা simple typo। আমি এখনই booking টা check করছি। (Pause) হ্যাঁ, দেখছি। "Ahemed" লেখা আছে।

**৬. Customer:** এটা কি ঠিক করা যাবে? আমার NID তে "Ahmed" আছে, airport এ কি সমস্যা হবে?

**৭. Agent:** Sir, domestic flight এ NID match করা হয়। Name এ spelling মিলমিশ না হলে boarding pass দিতে অনেক সময় issue হয়। তাই correction করা জরুরি।

**৮. Customer:** তাহলে তাড়াতাড়ি করুন। কাল সকাল ৮টায় flight।

**৯. Agent:** Sir, US-Bangla Airlines এর ticket হওয়ায় correction request আমাদের থেকে airline এ পাঠাতে হবে। আমি এখনই ticket টা flag করছি।

**১০. Customer:** Correction করতে কি extra charge লাগবে?

**১১. Agent:** Sir, domestic airline এ minor spelling correction সাধারণত free হয়। তবে এটা airline এর discretion এ নির্ভর করে। US-Bangla সাধারণত এক অক্ষরের typo free তে correct করে।

**১২. Customer:** Free তে হলে তো ভালো। কিন্তু আজকে রাতের মধ্যেই হবে তো? Flight কাল সকালে।

**১৩. Agent:** Sir, আমি এখনই emergency name correction request পাঠাচ্ছি। আমাদের airline liaison team টি ২৪ ঘণ্টা active। সাধারণত ২-৩ ঘণ্টার মধ্যে confirmation আসে।

**১৪. Customer:** ২-৩ ঘণ্টার মধ্যে confirm হলে রাতের মধ্যেই পাবো। ঠিক আছে।

**১৫. Agent:** Sir, correction confirmed হলে আমি আপনার registered email এ নতুন e-ticket পাঠিয়ে দেবো। আপনার email address confirm করবেন একটু?

**১৬. Customer:** Email হচ্ছে salam.ahmed99@gmail.com।

**১৭. Agent:** Noted sir। আমি request টা এখনই submit করছি। Reference number টা আমি SMS এ পাঠাচ্ছি।

**১৮. Customer:** ঠিক আছে। আর যদি কোনো charge আসে তাহলে কীভাবে জানাবেন?

**১৯. Agent:** Sir, charge applicable হলে confirmation এর আগেই আমরা আপনাকে call করে জানাবো। আপনার approval ছাড়া কোনো charge করা হবে না।

**২০. Customer:** ঠিক আছে ফাহিম সাহেব। রাতের মধ্যে update পাবো তো?

**২১. Agent:** Sir, রাত ১১টার মধ্যে আপনার email এ updated ticket আসার কথা। কোনো সমস্যা হলে এই number এ call করুন।

**২২. Customer:** ঠিক আছে। ধন্যবাদ।

**২৩. Agent:** ভালো থাকবেন sir। আপনার Chittagong trip সুন্দর হোক। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৬ঃ Sajek Valley tour package এ ১৫ জনের group এর কথা বলা হয়েছিল কিন্তু মাত্র ৪ জন এসেছে

> Customer GoZayaan থেকে Sajek Valley ট্যুর প্যাকেজ কিনেছিলেন। Sales agent তাকে বলেছিলেন ১৫-২০ জনের একটি লাইভলি গ্রুপ থাকবে। কিন্তু ট্যুরের দিনে মাত্র ৪ জন দেখে customer মনে করছেন তাকে mislead করা হয়েছে।

**১. Agent:** শুভ সকাল, 'GoZayaan' support থেকে আমি Tisha বলছি। কীভাবে assist করতে পারি?

**২. Customer:** তিশা আপু, আমি Sajek Valley tour package নিয়েছিলাম। Tour guide বলেছিল ১৫-২০ জনের group। আজ দেখি মোট ৪ জন! আমি কি scam এর শিকার হয়েছি?

**৩. Agent:** Mam, এটা শুনে আমি সত্যিই concerned। Kindly booking ID টা বলবেন? আমি tour package এর details দেখছি।

**৪. Customer:** Booking ID GZ-556677। Sales এর সময় বলা হয়েছিল এটা group departure, ১৫ জনের কম হলে tour হবে না। কিন্তু আজ মাত্র ৪ জন!

**৫. Agent:** Mam, আমি package details check করছি। (Pause) আমি দেখছি এটা 'Group Departure' package, minimum 10 persons requirement আছে। মাত্র ৪ জন নিয়ে tour চালানো আমাদের terms এর বাইরে।

**৬. Customer:** তাহলে কেন tour operator আমাদের নিয়ে বের হচ্ছে? এটা কি ঠিক হচ্ছে?

**৭. Agent:** Mam, সেটা operator এর সিদ্ধান্ত। তবে group size এর guarantee যদি আপনাকে দেওয়া হয়ে থাকে এবং তা পূরণ না হয়, তাহলে আপনি refund বা রeschedule এর request করতে পারেন।

**৮. Customer:** আমি tour cancel করতে চাই। কিন্তু আমি তো ইতিমধ্যে travel করে এখানে চলে এসেছি।

**৯. Agent:** Mam, এই situation টা complex। আপনি tour cancel করলে package amount আমাদের cancellation policy অনুযায়ী partial refund হবে। তবে আপনার যাতায়াত খরচ GoZayaan এর আওতায় পড়বে না।

**১০. Customer:** তাহলে কি tour continue করাই ভালো? ৪ জন নিয়ে হলেও?

**১১. Agent:** Mam, আমি honestly বলছি। Tour continue করলে Sajek এর সৌন্দর্য তো উপভোগ করতে পারবেন। Group small হলেও destination এর experience কিন্তু same।

**১২. Customer:** হুম, কিন্তু sales এর সময় false information দেওয়া হয়েছে। এর জন্য কি GoZayaan কিছু করবে?

**১৩. Agent:** Mam, এটা আমাদের sales team এর একটা serious lapse। আমি এই call টার পরেই investigation শুরু করছি।

**১৪. Customer:** আমি চাই compensation। কারণ group এর কথা বলে আমাকে package sell করা হয়েছে।

**১৫. Agent:** Mam, আপনার demand টা reasonable। আমি আপনার account এ ১,৫০০ টাকার travel credit এবং next group tour এ ২০% discount offer করতে পারি।

**১৬. Customer:** ১,৫০০ টাকা credit আর ২০% discount — এটা acceptable। Tour তো শেষ করেই যাবো, এতদূর এসেছি।

**১৭. Agent:** Mam, ঠিক আছে। আমি credit আজকেই apply করছি এবং sales agent এর বিরুদ্ধে formal disciplinary action নেওয়া হবে।

**১৮. Customer:** ঠিক আছে তিশা আপু। Tour guide কে বলবেন ৪ জনকে ভালো service দিতে।

**১৯. Agent:** অবশ্যই mam। আমি tour guide কে সরাসরি call করে inform করছি যেন আপনাদের experience টা excellent হয়।

**২০. Customer:** Thank you, that's all I need।

**২১. Agent:** Mam, Sajek Valley উপভোগ করুন। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৭ঃ Customer ৩টি airline compare করে সবচেয়ে সস্তা Dhaka-Dubai fare খুঁজছেন — baggage সহ

> Customer GoZayaan helpline এ call করে Dhaka-Dubai route এর জন্য Biman, Emirates এবং Air Arabia র fare comparison জানতে চাইছেন। তিনি চান সবচেয়ে কম খরচে ২৩ kg checked baggage সহ ticket।

**১. Agent:** শুভ দুপুর, 'GoZayaan' থেকে আমি Hasan বলছি। কীভাবে assist করতে পারি?

**২. Customer:** হাসান ভাই, আমি Dubai যাবো আগামী মাসে। ৩টা airline এর comparison জানতে চাই। Biman, Emirates আর Air Arabia।

**৩. Agent:** Sir, আমি এখনই সেরা available fares check করছি। Travel date এবং return আছে কিনা বলবেন?

**৪. Customer:** One way, আগামী মাসের ১৫ তারিখে। আর অবশ্যই ২৩ kg checked baggage সহ।

**৫. Agent:** Sir, baggage included fare check করছি। (Pause) আমি তিনটি airline এর best available rates পেয়েছি।

**৬. Customer:** বলুন, কোনটায় কত পড়বে?

**৭. Agent:** Sir, Biman Bangladesh Airlines: ৩৮,৫০০ টাকা, baggage included, direct flight, travel time ৬ ঘণ্টা। Air Arabia: ৩২,০০০ টাকা, baggage included তবে Sharjah airport এ ১.৫ ঘণ্টার layover আছে। Emirates: ৫৫,০০০ টাকা, direct flight, baggage included, premium service।

**৮. Customer:** Air Arabia তে layover থাকলেও price টা অনেক কম। Sharjah থেকে Dubai কতটা দূর?

**৯. Agent:** Sir, Sharjah international airport থেকে Dubai city centre প্রায় ২০ কিলোমিটার। Taxi বা metro তে ৩০-৪৫ মিনিট লাগে।

**১০. Customer:** আচ্ছা। তাহলে Air Arabia তে গেলে Sharjah নামতে হবে, Dubai না। এটা কি সমস্যা?

**১১. Agent:** Sir, অনেক traveller এই route ব্যবহার করেন। Sharjah থেকে Dubai যাওয়া খুবই convenient। Airport থেকে direct bus ও পাওয়া যায়।

**১২. Customer:** Cost কত পড়বে Sharjah থেকে Dubai যেতে?

**১৩. Agent:** Sir, RTA bus এ মাত্র ৫-৭ AED (প্রায় ২২০-৩০০ টাকা) এ Dubai পৌঁছানো যায়। Taxi তে ৩০-৪০ AED হতে পারে।

**১৪. Customer:** তাহলে Air Arabia র সাথে extra ৩০০ টাকা যোগ করলেও ৩২,৩০০ টাকা, Biman এর চেয়ে ৬,০০০+ টাকা কম। Air Arabia ই ভালো মনে হচ্ছে।

**১৫. Agent:** Sir, budget এর দিক থেকে Air Arabia excellent choice। তবে একটা বিষয়, Biman direct flight হওয়ায় কম ক্লান্তিকর। আপনি যদি long travel এ comfortable থাকেন তাহলে Air Arabia নিতে পারেন।

**১৬. Customer:** আমি ওভাবে ভাবিনি। Direct না হলে কি কোনো risk আছে?

**১৭. Agent:** Sir, Air Arabia একটি reputable airline, layover risk খুব কম। তবে যদি কোনো flight delay হয়, connecting flight miss হওয়ার ক্ষীণ সম্ভাবনা থাকে। তবে ১.৫ ঘণ্টার layover যথেষ্ট buffer।

**১৮. Customer:** ঠিক আছে। Air Arabia তে book করবো। কিন্তু আজকে কি rate টা lock করা যাবে?

**১৯. Agent:** Sir, air fares dynamic, তাই আজকের rate পরিবর্তন হতে পারে। আমি এখনই আপনার জন্য seat hold করতে পারি ২৪ ঘণ্টার জন্য, payment কাল করলেও চলবে।

**২০. Customer:** এটা ভালো option। ২৪ ঘণ্টার hold করে রাখুন।

**২১. Agent:** Sir, আমি seat hold করে দিচ্ছি। আপনার email এ hold confirmation পাঠাচ্ছি। কাল রাত ১২টার মধ্যে payment করলেই booking confirmed হবে।

**২২. Customer:** ঠিক আছে হাসান ভাই, ধন্যবাদ সুন্দর comparison এর জন্য।

**২৩. Agent:** আপনার Dubai trip সুন্দর হোক sir। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৮ঃ Outbound call — Flight এর আগের দিন boarding pass, terminal info এবং weather advisory পাঠানো

> Customer এর আগামীকাল সকালে Dhaka-Kolkata flight। GoZayaan agent outbound call করে boarding pass summary, airport terminal information এবং destination এর weather update দিচ্ছেন।

**১. Agent:** শুভ বিকাল, 'GoZayaan' থেকে আমি Nabil বলছি। আমি কি রাহেলা ম্যামের সাথে কথা বলছি?

**২. Customer:** হ্যাঁ, আমি রাহেলা বলছি।

**৩. Agent:** Mam, আপনার আগামীকাল GoZayaan এর মাধ্যমে book করা Kolkata flight আছে। একটি pre-travel update দেওয়ার জন্য call করছিলাম।

**৪. Customer:** ওহ হ্যাঁ! ঠিক মনে করিয়ে দিলেন। কী কী জানাবেন?

**৫. Agent:** Mam, আপনার flight IndiGo 6E-1401, departure Hazrat Shahjalal International Airport থেকে সকাল ৯:৩০ AM। আপনাকে কমপক্ষে সকাল ৭:১৫ AM এর মধ্যে airport এ থাকতে হবে।

**৬. Customer:** ঠিক আছে। International terminal এ যেতে হবে, তাই তো?

**৭. Agent:** Mam, জ্বী। Terminal ৩, international departure। Check-in counter IndiGo এর জন্য G-wing এ, gate number 7।

**৮. Customer:** Boarding pass কি আমার email এ পাঠিয়ে দেবেন?

**৯. Agent:** Mam, আপনার registered email এ e-boarding pass পাঠিয়ে দিচ্ছি। তবে আপনি চাইলে IndiGo র web check-in নিজেও করতে পারবেন, flight এর ৪৮ ঘণ্টা আগে থেকে সেটা open হয়।

**১০. Customer:** Web check-in করলে কি airport এ আলাদা counter আছে?

**১১. Agent:** Mam, হ্যাঁ। Web check-in করা থাকলে আপনি directly 'Baggage Drop' counter এ যেতে পারবেন, regular check-in queue তে দাঁড়াতে হবে না।

**১২. Customer:** বাহ, এটা তো সময় বাঁচাবে। Kolkata এর weather কেমন আছে?

**১৩. Agent:** Mam, আগামীকাল Kolkata তে আংশিক মেঘলা আবহাওয়া থাকবে। Temperature হবে ২৮-৩২ ডিগ্রি। দুপুরের দিকে হালকা বৃষ্টির সম্ভাবনা আছে, ছাতা সাথে রাখলে ভালো হবে।

**১৪. Customer:** আচ্ছা, ছাতা নেবো। Baggage allowance কত?

**১৫. Agent:** Mam, আপনার ticket এ ২০ kg checked baggage এবং ৭ kg carry-on bag allowance আছে। Liquid items carry-on এ ১০০ml limit মনে রাখবেন।

**১৬. Customer:** Okay, noted। Kolkata airport থেকে hotel যেতে হবে, কোনো suggestion আছে?

**১৭. Agent:** Mam, Netaji Subhas Chandra Bose International Airport থেকে city centre যেতে pre-paid taxi সবচেয়ে safe। Airport এর বাইরে official prepaid counter থেকে নিলে overcharge হওয়ার ঝুঁকি নেই। Metro ও available তবে luggage নিয়ে একটু কঠিন।

**১৮. Customer:** Pre-paid taxi ই নেবো। ধন্যবাদ নাবিল সাহেব, অনেক helpful information দিলেন।

**১৯. Agent:** Mam, আপনার সুবিধার জন্যই আমাদের এই pre-travel service। Flight number, terminal এবং weather summary সহ একটি SMS ও পাঠিয়ে দিচ্ছি।

**২০. Customer:** Perfect। আর কিছু জানার দরকার নেই।

**২১. Agent:** Mam, safe flight এবং Kolkata এ আনন্দময় সময় কামনা করছি। 'GoZayaan' এ call করার জন্য ধন্যবাদ।

---

## Scenario ৯ঃ Couple এর Maldives honeymoon package — budget এর মধ্যে water villa upgrade চাইছেন

> নবদম্পতি GoZayaan থেকে Maldives honeymoon package বুক করেছেন। তারা package এ যে beach bungalow দেওয়া হয়েছে সেটাকে water villa তে upgrade করতে চাইছেন এবং budget এর মধ্যে কোনো সুযোগ আছে কিনা জানতে call করেছেন।

**১. Agent:** শুভ সন্ধ্যা, 'GoZayaan' থেকে আমি Tisha বলছি। কীভাবে assist করতে পারি?

**২. Customer:** তিশা আপু, আমরা সদ্য বিয়ে করেছি। Maldives honeymoon package এ আছি। কিন্তু water villa তে একটু upgrade করতে চাইছিলাম।

**৩. Agent:** Mam, congratulations on your wedding! Honeymoon এর জন্য Maldives সত্যিই magical choice। Kindly আপনার booking ID বলবেন?

**৪. Customer:** Booking ID GZ-112244। আমরা সানি বিচ resort এর beach bungalow package এ আছি। Water villa এর দাম কত extra হবে?

**৫. Agent:** Mam, আমি আপনার booking এবং সেই resort এর upgrade option দেখছি। (Pause) Mam, আপনার current beach bungalow package এ ৫ রাত আছে। Water villa upgrade এর জন্য প্রতি রাতে additional ১৫,০০০ টাকা লাগবে।

**৬. Customer:** ৫ রাতের জন্য মানে ৭৫,০০০ টাকা extra! এটা তো অনেক বেশি। কোনো cheaper option নেই?

**৭. Agent:** Mam, full upgrade এর alternative হিসেবে আমাদের কাছে একটি option আছে। আপনি ৫ রাতের মধ্যে শুধু ২ রাত water villa তে কাটাতে পারেন এবং বাকি ৩ রাত beach bungalow এই থাকতে পারেন।

**৮. Customer:** ২ রাত water villa তে থাকলে extra চার্জ হবে ৩০,০০০ টাকা। এটা কি একটু কমানো যাবে?

**৯. Agent:** Mam, আমি resort এর সাথে কথা বলতে পারি। Honeymoon couple দের জন্য তারা অনেক সময় special arrangement করে। একটু hold করবেন?

**১০. Customer:** অবশ্যই।

**১১. Agent:** (Pause) Mam, সুখবর! Resort কর্তৃপক্ষ honeymoon couple দের জন্য ২ রাতের water villa upgrade এ ২০% discount দিচ্ছে। মোট extra charge হবে ২৪,০০০ টাকা।

**১২. Customer:** ৩০,০০০ থেকে ২৪,০০০ — ৬,০০০ টাকা বাঁচলো। এটা acceptable। কিন্তু কোন ২ রাতে water villa পাবো?

**১৩. Agent:** Mam, আপনি কোন ২ রাত prefer করবেন? First 2 nights নাকি শেষের ২ রাত?

**১৪. Customer:** Arrival এর পর প্রথম ২ রাত beach bungalow এ settle হই, তারপর মাঝের ২ রাত water villa তে থাকলে ভালো হবে।

**১৫. Agent:** Mam, তার মানে রাত ৩ এবং রাত ৪ water villa তে। আমি এখনই resort এ confirm করছি।

**১৬. Customer:** Perfect। আর water villa তে কি breakfast included থাকবে?

**১৭. Agent:** Mam, হ্যাঁ। আপনার current package এ already breakfast included আছে, water villa তেও same service পাবেন। তবে sunset cruise এবং spa সার্ভিস গুলো additional।

**১৮. Customer:** Sunset cruise এর কথা বললেন, সেটা কি arrange করা যাবে?

**১৯. Agent:** Mam, অবশ্যই। Honeymoon couple দের জন্য private sunset cruise টা সত্যিই unforgettable। এটা প্রায় ৮,০০০ টাকায় arrange করা যায়।

**২০. Customer:** সেটাও add করে দিন। Total extra কত হলো?

**২১. Agent:** Mam, water villa upgrade ২৪,০০০ টাকা এবং sunset cruise ৮,০০০ টাকা — মোট ৩২,০০০ টাকা additional। আমি payment link পাঠিয়ে দিচ্ছি।

**২২. Customer:** ঠিক আছে তিশা আপু। আমাদের honeymoon টা আরও special হবে।

**২৩. Agent:** Mam, আপনার honeymoon অনেক সুন্দর হোক। 'GoZayaan' এর পক্ষ থেকে নবদম্পতিকে আন্তরিক শুভেচ্ছা।

---

## Scenario ১০ঃ Outbound call — Post-trip follow-up, Google review request এবং next booking এ ১০% discount offer

> Customer সম্প্রতি GoZayaan এর মাধ্যমে Chittagong trip থেকে ফিরেছেন। Agent post-trip follow-up call করে experience জানতে চাইছেন, Google review এর request করছেন এবং next booking এ loyalty discount অফার করছেন।

**১. Agent:** শুভ সকাল, 'GoZayaan' থেকে আমি Fahim বলছি। আমি কি রাফি সাহেবের সাথে কথা বলছি?

**২. Customer:** হ্যাঁ, রাফি বলছি। কী ব্যাপার?

**৩. Agent:** Sir, আপনি গত সপ্তাহে GoZayaan এর মাধ্যমে Chittagong trip করেছিলেন। Trip কেমন হলো জানতে call করলাম।

**৪. Customer:** আরে হ্যাঁ! Trip টা overall ভালোই ছিল। Hotel টা দারুণ ছিল, কিন্তু একটু সমস্যা হয়েছিল।

**৫. Agent:** Sir, কী সমস্যা হয়েছিল? জানালে আমরা ভবিষ্যতে improve করতে পারবো।

**৬. Customer:** Hotel এ check-in এ প্রায় ১ ঘণ্টা delay হয়েছিল। Room ready ছিল না, আমাকে lobby তে বসে থাকতে হয়েছে।

**৭. Agent:** Sir, এটা সত্যিই বিরক্তিকর experience। এই feedback টা আমাদের hotel partner কে জানানো হবে যেন future guest দের এই সমস্যায় পড়তে না হয়।

**৮. Customer:** ঠিক আছে। Hotel এর বাইরে বাকি সব কিন্তু ভালো ছিল, আপনাদের booking process, confirmation, সব smooth ছিল।

**৯. Agent:** Thank you sir। এটা শুনে ভালো লাগলো। Sir, আপনার কাছে একটি ছোট অনুরোধ ছিল।

**১০. Customer:** কী অনুরোধ?

**১১. Agent:** Sir, আপনি যদি Google এ বা GoZayaan app এ আপনার trip experience নিয়ে একটা review দিতেন, তাহলে অনেক নতুন traveller উপকৃত হতেন।

**১২. Customer:** Review দিতে আমার সময় লাগবে। সহজে কীভাবে দেওয়া যাবে?

**১৩. Agent:** Sir, আমি আপনার WhatsApp এ একটি direct review link পাঠিয়ে দিচ্ছি। Click করলেই আপনার booking auto-populate হবে, শুধু কয়েকটা line লিখলেই হবে।

**১৪. Customer:** এত সহজ হলে দিয়ে দেবো। ৫ minute এর কাজ।

**১৫. Agent:** Sir, অসংখ্য ধন্যবাদ। আর আপনার জন্য একটা special offer আছে।

**১৬. Customer:** কী offer?

**১৭. Agent:** Sir, আপনি GoZayaan এর valued customer হওয়ায় আপনার next booking এ automatically ১০% loyalty discount apply হবে। এই offer টি আগামী ৩ মাস valid।

**১৮. Customer:** ১০% discount! সেটা তো অনেক ভালো। আমি আসলে শীতের সময় Sundarbans যাওয়ার plan করছি।

**১৯. Agent:** Sir, Sundarbans! দারুণ choice। আমাদের কাছে November-December এ exclusive Sundarbans winter package আছে। আগে থেকে book করলে আরও ভালো deal পাবেন।

**২০. Customer:** আগামী মাস থেকে plan করবো। GoZayaan এই করবো।

**২১. Agent:** Sir, আমাদের app এ 'Sundarbans' search করলেই সব package দেখতে পাবেন। কোনো প্রশ্ন থাকলে helpline এ call করবেন।

**২২. Customer:** ঠিক আছে ফাহিম সাহেব। Review লিংক পাঠান, আজকেই দিয়ে দেবো।

**২৩. Agent:** Sir, link পাঠিয়ে দিচ্ছি। আপনার পরবর্তী trip আরও enjoyable হোক। 'GoZayaan' এর সাথে থাকার জন্য অসংখ্য ধন্যবাদ।

---
