# দারাজ (Daraz) কাস্টমার সার্ভিস কল সেন্টার স্ক্রিপ্ট

**ডোমেইন:** জেনারেল ই-কমার্স (E-commerce Marketplace)  
**মোট সিনারিও:** ১০০+


---


## সিনারিও ১ঃ অর্ডার ৫ দিন ধরে "Shipped" দেখাচ্ছে, কোনো tracking update নেই

> একজন কাস্টমার ৫ দিন আগে একটি ব্যাকপ্যাক অর্ডার করেছিলেন। অর্ডার "Shipped" স্ট্যাটাসে আটকে আছে, কোনো tracking update আসছে না। কাস্টমার উদ্বিগ্ন যে পার্সেল হারিয়ে গেছে কিনা। Agent সিস্টেমে চেক করে দেখেন পার্সেলটি একটি sorting hub-এ আটকে আছে এবং courier-এর সাথে coordinate করে সমাধান করেন।

**১. এজেন্টঃ** Daraz customer care-এ কল করার জন্য ধন্যবাদ। আমি সাবরিনা, আপনাকে কীভাবে সাহায্য করতে পারি?

**২. কাস্টমারঃ** আপু, আমি ৫ দিন আগে একটা ব্যাকপ্যাক অর্ডার করেছিলাম। এখনো পাইনি, tracking-এ শুধু "Shipped" লেখা, কোনো update নেই।

**৩. এজেন্টঃ** sir, অসুবিধার জন্য দুঃখিত। আমি এখনই আপনার অর্ডারটি চেক করছি। আপনার order ID টা একটু বলবেন?

**৪. কাস্টমারঃ** Order ID হচ্ছে DZ-৫৬৭৮৯০১২৩। আমার নাম শাকিল আহমেদ, নম্বর ০১৭১২৩৪৫৬৭৮।

**৫. এজেন্টঃ** ধন্যবাদ শাকিল sir, তথ্য verify হয়ে গেছে। আমি আপনার অর্ডারের shipment details দেখছি, একটু অপেক্ষা করুন।

**৬. কাস্টমারঃ** আপু, ৫ দিন হয়ে গেছে কিন্তু একটাও tracking update আসেনি। পার্সেলটা কি হারিয়ে গেছে?

**৭. এজেন্টঃ** sir, আমি দেখতে পাচ্ছি আপনার পার্সেলটি গাজীপুরের একটি sorting hub-এ ৩ দিন ধরে আটকে আছে। বিস্তারিত বুঝিয়ে বলছি — মাঝে মাঝে peak season-এ বা অতিরিক্ত shipment load থাকলে sorting hub-এ parcel processing-এ দেরি হয়। আপনার পার্সেলটি হারিয়ে যায়নি, শুধু queue-তে আটকে আছে। আমি এখনই courier team-কে escalate করছি যাতে আপনার পার্সেলটি priority-তে dispatch হয়।

**৮. কাস্টমারঃ** গাজীপুরে আটকে আছে? আমি তো মিরপুরে থাকি, কবে নাগাদ পাবো আপু?

**৯. এজেন্টঃ** sir, আমি courier team-এর সাথে coordinate করে আপনার পার্সেলটি urgent tag দিয়ে দিয়েছি। আগামী ২৪ থেকে ৪৮ ঘণ্টার মধ্যে delivery হওয়ার কথা।

**১০. কাস্টমারঃ** ৪৮ ঘণ্টা! আপু, আমি তো এই ব্যাগটা office trip-এর জন্য কিনেছিলাম, পরশু রওনা দেবো। সময়মতো না পেলে তো কোনো লাভ নেই।

**১১. এজেন্টঃ** sir, আপনার urgency আমি বুঝতে পারছি। আমি এই মুহূর্তে delivery hub-এর supervisor-কে আলাদাভাবে mark করে দিচ্ছি যে এটি time-sensitive delivery। আশা করি আগামীকালের মধ্যেই পেয়ে যাবেন।

**১২. কাস্টমারঃ** আচ্ছা আপু, কিন্তু যদি আগামীকাল না আসে তাহলে কি আমি order cancel করে refund নিতে পারবো?

**১৩. এজেন্টঃ** জ্বী sir, অবশ্যই পারবেন। যদি ৪৮ ঘণ্টার মধ্যে delivery না হয়, আপনি app থেকে অথবা আমাদের call করে cancel request দিতে পারবেন এবং full refund পাবেন।

**১৪. কাস্টমারঃ** Refund কিভাবে আসবে? আমি bKash দিয়ে payment করেছিলাম।

**১৫. এজেন্টঃ** sir, bKash দিয়ে payment করে থাকলে refund সরাসরি আপনার bKash account-এ ফেরত যাবে। সাধারণত ৫ থেকে ৭ কর্মদিবস সময় লাগে refund process হতে।

**১৬. কাস্টমারঃ** ৫ থেকে ৭ দিন! এতো সময় কেন আপু? টাকা তো সাথে সাথে কেটে নিয়েছিল।

**১৭. এজেন্টঃ** sir, আপনার কথা যুক্তিসংগত। তবে refund-এর ক্ষেত্রে Daraz-এর finance team verification করে তারপর bKash gateway-তে পাঠায়, সেখানে আরেকটি processing হয়। তাই মোট কিছুটা সময় লাগে। তবে বেশিরভাগ ক্ষেত্রে ৩ দিনের মধ্যেই হয়ে যায়।

**১৮. কাস্টমারঃ** আচ্ছা বুঝলাম আপু। তাহলে আমি আগামীকাল পর্যন্ত অপেক্ষা করি। কিন্তু tracking update কি আসবে এবার?

**১৯. এজেন্টঃ** জ্বী sir, আমি courier-কে বলে দিয়েছি আপনার পার্সেলটি hub থেকে বের হওয়ার সাথে সাথে tracking update পাঠাতে। আপনার phone-এ SMS-ও আসবে।

**২০. কাস্টমারঃ** ঠিক আছে আপু। আচ্ছা, ভবিষ্যতে এই ধরনের delay এড়াতে কি Daraz Express courier select করা ভালো হবে?

**২১. এজেন্টঃ** sir, খুব ভালো প্রশ্ন। Daraz Express হচ্ছে আমাদের নিজস্ব delivery service, সেটা সাধারণত ২ থেকে ৩ দিনের মধ্যে deliver করে। Order করার সময় যদি "Daraz Express" badge দেখেন seller-এর পাশে, তাহলে সেই seller থেকে কেনা ভালো।

**২২. কাস্টমারঃ** বুঝেছি আপু, পরের বার সেটা দেখে কিনবো। আপনার complaint reference number টা দিন একটু।

**২৩. এজেন্টঃ** sir, আপনার complaint reference number হচ্ছে DZ-CMP-২০২৬০৭২১-০০১। এটা সংরক্ষণ করে রাখুন। ৪৮ ঘণ্টার মধ্যে delivery না হলে এই reference দিয়ে আবার call করবেন।

**২৪. কাস্টমারঃ** নোট করে রাখলাম আপু। ধন্যবাদ সাবরিনা আপু, আশা করি আগামীকাল পার্সেলটা পেয়ে যাবো।

**২৫. এজেন্টঃ** আমিও আশা করি sir। Daraz-এ কেনাকাটা করার জন্য ধন্যবাদ, শুভ দিন কাটুক।

---

## সিনারিও ২ঃ ডেলিভারি ম্যান "Delivered" মার্ক করেছে কিন্তু কাস্টমার পার্সেল পাননি

> একজন মহিলা কাস্টমার রাগান্বিত হয়ে কল করেন কারণ তার অর্ডার করা একটি হেয়ার ড্রায়ারের tracking-এ "Delivered" দেখাচ্ছে, কিন্তু তিনি কোনো পার্সেল পাননি। দরজায় কেউ আসেনি, কোনো কল পাননি। Agent investigation শুরু করেন এবং delivery rider-এর GPS log ও photo proof চেক করে দেখেন rider ভুল বাসায় deliver করেছে।

**১. কাস্টমারঃ** হ্যালো, আমি অত্যন্ত বিরক্ত হয়ে কল করছি! আমার অর্ডারে "Delivered" লেখা দেখাচ্ছে কিন্তু আমি কোনো পার্সেল পাইনি। এটা কী ধরনের সার্ভিস?

**২. এজেন্টঃ** ম্যাম, আমি তানিম বলছি Daraz customer care থেকে। আপনার বিরক্তি সম্পূর্ণ যুক্তিসংগত এবং আমি এই বিষয়টি গুরুত্বের সাথে দেখছি। আপনার order ID টা বলবেন?

**৩. কাস্টমারঃ** Order ID হচ্ছে DZ-৯৮৭৬৫৪৩২১। আমার নাম ফারজানা আক্তার। আমি ধানমণ্ডিতে থাকি, ৫ নম্বর রোডে।

**৪. এজেন্টঃ** ধন্যবাদ ফারজানা ম্যাম, আমি আপনার অর্ডারটি pull করছি। একটু অপেক্ষা করুন, আমি delivery rider-এর GPS log এবং delivery proof চেক করছি।

**৫. কাস্টমারঃ** ভাইয়া, আমি সারাদিন বাসায় ছিলাম। দরজায় কেউ আসেনি, কোনো ফোন কলও পাইনি। তারপরও "Delivered" মার্ক করে দিয়েছে, এটা তো প্রতারণা!

**৬. এজেন্টঃ** ম্যাম, আমি সম্পূর্ণ বুঝতে পারছি আপনার হতাশা। আমি delivery rider-এর records চেক করে দেখছি। বিস্তারিত বলছি — আমাদের system-এ delivery confirm করার সময় rider-কে একটি photo proof upload করতে হয় এবং GPS location record হয়। আমি দেখছি rider একটি photo upload করেছে, কিন্তু GPS location আপনার address থেকে প্রায় ৩০০ মিটার দূরে দেখাচ্ছে। সম্ভবত rider ভুল বাসায় পার্সেলটি দিয়ে এসেছে।

**৭. কাস্টমারঃ** মানে অন্য কারো বাসায় আমার পার্সেল দিয়ে এসেছে? তাহলে এখন কী হবে?

**৮. এজেন্টঃ** ম্যাম, আমি এখনই delivery rider-কে call করে বিষয়টা confirm করছি এবং তাকে সঠিক address-এ পার্সেল পৌঁছে দিতে বলছি। আমি আপনাকে একটু hold-এ রাখছি, ২ মিনিট সময় দিন।

**৯. কাস্টমারঃ** আচ্ছা, আমি hold-এ আছি। কিন্তু তাড়াতাড়ি করুন।

**১০. এজেন্টঃ** ম্যাম, ধন্যবাদ অপেক্ষার জন্য। আমি rider-এর সাথে কথা বলেছি। সে স্বীকার করেছে যে আপনার বিল্ডিং-এর পাশের বিল্ডিং-এ ভুলে পার্সেলটি একজন security guard-এর কাছে দিয়ে এসেছে।

**১১. কাস্টমারঃ** পাশের বিল্ডিং-এ! ভাইয়া, এটা তো মারাত্মক গাফিলতি। আমি কিভাবে পাশের বিল্ডিং-এ গিয়ে খুঁজবো?

**১২. এজেন্টঃ** ম্যাম, আপনাকে কোথাও যেতে হবে না। আমি rider-কে বলেছি সে নিজে এখনই পাশের বিল্ডিং থেকে পার্সেলটি নিয়ে আপনার সঠিক ঠিকানায় পৌঁছে দেবে। সে ৩০ মিনিটের মধ্যে আসবে।

**১৩. কাস্টমারঃ** ৩০ মিনিট? ঠিক আছে, কিন্তু যদি পার্সেলটি ইতিমধ্যে কেউ খুলে ফেলে থাকে বা damaged হয়ে থাকে?

**১৪. এজেন্টঃ** ম্যাম, পার্সেল পাওয়ার পর আপনি অবশ্যই খুলে দেখবেন। যদি product damaged থাকে বা কোনো সমস্যা থাকে, তাহলে সাথে সাথে আমাদের call করবেন। আমরা immediate replacement অথবা full refund process করে দেবো।

**১৫. কাস্টমারঃ** আচ্ছা। আর এই rider-এর বিরুদ্ধে কি কোনো ব্যবস্থা নেওয়া হবে? এই ধরনের ভুল তো গ্রহণযোগ্য না।

**১৬. এজেন্টঃ** ম্যাম, আমি rider-এর বিরুদ্ধে একটি formal complaint log করেছি। আমাদের delivery operations team এটি review করবে এবং যথাযথ ব্যবস্থা নেবে। Repeated offense হলে rider-কে deactivate করা হয়।

**১৭. কাস্টমারঃ** ভালো, এটা শুনে একটু ভালো লাগলো। ভাইয়া, আমি কিন্তু আগেও একবার এই ধরনের সমস্যায় পড়েছিলাম। মনে হচ্ছে আপনাদের delivery system-এ গুরুতর সমস্যা আছে।

**১৮. এজেন্টঃ** ম্যাম, আপনার অভিজ্ঞতার জন্য আমরা আন্তরিকভাবে দুঃখিত। আমি আপনার account-এ একটি special note রাখছি যাতে ভবিষ্যতে আপনার delivery-তে extra verification করা হয়। এছাড়া আপনার অসুবিধার জন্য আপনার Daraz account-এ ১০০ টাকার একটি compensation voucher add করে দিচ্ছি।

**১৯. কাস্টমারঃ** ১০০ টাকার voucher? আচ্ছা সেটা তো পেলাম, ধন্যবাদ। কিন্তু পরের বার delivery-র সময় কি আমাকে আগে call করতে বলা যায়?

**২০. এজেন্টঃ** জ্বী ম্যাম, আপনার address-এ delivery instruction-এ "অবশ্যই কাস্টমারকে আগে call করবেন" লিখে দিচ্ছি। এটা rider-এর screen-এ দেখাবে। এছাড়া Daraz app-এর settings-এ "Delivery Preferences" section-এ গিয়ে আপনিও এই instruction add করতে পারবেন।

**২১. কাস্টমারঃ** আচ্ছা ভাইয়া, সেটা করে রাখবো। ঠিক আছে, তাহলে ৩০ মিনিট অপেক্ষা করি rider আসার জন্য।

**২২. এজেন্টঃ** জ্বী ম্যাম। rider এসে আপনাকে call করবে। পার্সেল পেয়ে কোনো সমস্যা থাকলে আমাদের reference number DZ-CMP-২০২৬০৭২১-০০২ দিয়ে call করবেন।

**২৩. কাস্টমারঃ** নোট করে রাখলাম। ধন্যবাদ তানিম ভাইয়া, আপনি ভালোভাবে handle করেছেন বিষয়টা।

**২৪. এজেন্টঃ** ধন্যবাদ ম্যাম, আপনার ধৈর্যের জন্য কৃতজ্ঞ। Daraz-এ কেনাকাটা চালিয়ে যান, ভালো থাকবেন।

---

## সিনারিও ৩ঃ সদ্য বাসা বদল করেছেন, পুরনো ঠিকানায় পার্সেল ডেলিভারি হয়ে গেছে

> একজন কাস্টমার সম্প্রতি উত্তরা থেকে বনানীতে বাসা বদল করেছেন কিন্তু Daraz app-এ পুরনো ঠিকানা update করতে ভুলে গেছেন। একটি ল্যাপটপ স্ট্যান্ড অর্ডার করেছিলেন যেটি পুরনো ঠিকানায় deliver হয়ে গেছে। পুরনো বাসায় এখন নতুন ভাড়াটে থাকেন। Agent rider-কে coordinate করেন পুরনো ঠিকানা থেকে পার্সেল collect করে নতুন ঠিকানায় পৌঁছে দিতে।

**১. কাস্টমারঃ** ভাইয়া, আমি বড় বিপদে পড়েছি! আমার order টা পুরনো বাসায় চলে গেছে, আমি তো এখন ওখানে থাকি না। কী করবো বুঝতে পারছি না!

**২. এজেন্টঃ** sir, আমি আরিফ বলছি Daraz customer care থেকে। চিন্তা করবেন না, আমি সমাধান করার চেষ্টা করছি। আপনার order ID টা বলুন।

**৩. কাস্টমারঃ** Order ID হচ্ছে DZ-১১২২৩৩৪৪৫। আমি গত সপ্তাহে উত্তরা থেকে বনানীতে shift করেছি, app-এ address change করতে ভুলে গেছি।

**৪. এজেন্টঃ** আচ্ছা sir, আমি দেখতে পাচ্ছি order টি গতকাল উত্তরা সেক্টর ৭ এর পুরনো ঠিকানায় delivered হয়ে গেছে। কেউ কি receive করেছে ওখানে?

**৫. কাস্টমারঃ** ভাইয়া, পুরনো বাসায় এখন নতুন ভাড়াটে থাকে। আমি তাদের চিনি না, তাদের নম্বরও নেই। বাড়িওয়ালার নম্বর আছে শুধু।

**৬. এজেন্টঃ** sir, বিষয়টা একটু জটিল হলেও সমাধানযোগ্য। আমি delivery rider-এর record দেখছি। বিস্তারিত বুঝিয়ে বলছি — আমাদের system-এ দেখাচ্ছে rider পার্সেলটি গতকাল বিকাল ৪:১৫ মিনিটে deliver করেছে এবং যিনি receive করেছেন তার নাম "মিসেস রহমান" লেখা আছে। আমি এখন rider-কে contact করে পুরনো ঠিকানা থেকে পার্সেল collect করার arrange করছি।

**৭. কাস্টমারঃ** কিন্তু ভাইয়া, যদি তারা পার্সেল খুলে ফেলে থাকে অথবা দিতে না চায়, তাহলে কী হবে?

**৮. এজেন্টঃ** sir, সেক্ষেত্রে আমাদের courier team সরাসরি visit করে পার্সেলটি collect করবে। তারা যদি না দেয় তাহলে আমরা আপনাকে full refund বা replacement-এর ব্যবস্থা করবো।

**৯. কাস্টমারঃ** আচ্ছা ভাইয়া। আমি বাড়িওয়ালাকে call করে বলি তিনি যেন নতুন ভাড়াটেকে বলেন পার্সেলটা রেখে দিতে?

**১০. এজেন্টঃ** sir, সেটা একটা ভালো idea। আপনি বাড়িওয়ালাকে জানান, আর আমি এদিক থেকে rider-কে পাঠাচ্ছি collect করতে। আপনার বনানীর নতুন ঠিকানাটা বলুন।

**১১. কাস্টমারঃ** বনানী রোড ১১, হাউস ২৫, ফ্ল্যাট B3। ভাইয়া, এটার জন্য কি আমাকে extra delivery charge দিতে হবে?

**১২. এজেন্টঃ** না sir, কোনো extra charge লাগবে না। এটা আমাদের delivery re-routing হিসেবে process হবে। তবে ভবিষ্যতে order দেওয়ার আগে অবশ্যই address verify করে নেবেন।

**১৩. কাস্টমারঃ** অবশ্যই ভাইয়া। আচ্ছা, আমি এখনই app-এ address update করে দিই। কিভাবে করবো?

**১৪. এজেন্টঃ** sir, Daraz app open করুন, নিচে "Account" tab-এ যান, তারপর "Address Book" option-এ click করুন। সেখানে পুরনো address edit বা delete করে নতুনটা default হিসেবে set করুন।

**১৫. কাস্টমারঃ** একটু wait করুন ভাইয়া, করছি। হ্যাঁ, নতুন address add করে default সেট করে দিলাম। পুরনোটা delete করবো?

**১৬. এজেন্টঃ** জ্বী sir, পুরনোটা delete করে দিন, তাহলে ভুল করে আবার সেটা select হওয়ার chance থাকবে না।

**১৭. কাস্টমারঃ** করে দিলাম ভাইয়া। পুরনো বাসা থেকে পার্সেল collect করতে কতক্ষণ লাগবে?

**১৮. এজেন্টঃ** sir, আমি rider-কে already assign করেছি। আজকের মধ্যে collect করে আগামীকাল সকালের মধ্যে আপনার বনানীর ঠিকানায় পৌঁছে দেওয়া হবে।

**১৯. কাস্টমারঃ** আগামীকাল সকাল? ঠিক আছে ভাইয়া, বাড়িওয়ালাকেও জানিয়ে দিচ্ছি এখনই।

**২০. এজেন্টঃ** sir, আর একটা পরামর্শ — প্রতিবার order place করার সময় checkout page-এ delivery address টা একবার চোখ বুলিয়ে নেবেন, তাহলে এই ভুল আর হবে না।

**২১. কাস্টমারঃ** হ্যাঁ ভাইয়া, এবার শিখে গেছি। অনেক ধন্যবাদ আরিফ ভাইয়া, ভালো থাকবেন।

**২২. এজেন্টঃ** আপনিও ভালো থাকবেন sir। Daraz-এ কেনাকাটা করার জন্য ধন্যবাদ, শুভকামনা।

---

## সিনারিও ৪ঃ ৩টি আইটেম অর্ডার করেছিলেন, মাত্র ২টি ডেলিভারি হয়েছে — Partial Delivery

> একজন গৃহিণী কাস্টমার রান্নাঘরের জন্য ৩টি আইটেম (ব্লেন্ডার, চপিং বোর্ড, মসলার জার সেট) একসাথে অর্ডার করেছিলেন। ডেলিভারি ম্যান ২টি আইটেম দিয়ে গেছে, ব্লেন্ডারটি নেই। কাস্টমার জানতে চান বাকি আইটেম কবে আসবে। Agent দেখেন ব্লেন্ডারটি আলাদা seller-এর কাছ থেকে আসছে এবং সেটি এখনো dispatch হয়নি।

**১. এজেন্টঃ** Daraz customer care, আমি নুসরাত। আপনাকে কীভাবে সাহায্য করতে পারি?

**২. কাস্টমারঃ** আপু, আমি তিনটা জিনিস একসাথে অর্ডার দিয়েছিলাম কিন্তু দুইটা এসেছে, ব্লেন্ডারটা আসেনি। আমি তো পুরো অর্ডারের টাকা দিয়ে দিয়েছি!

**৩. এজেন্টঃ** ম্যাম, আপনার অভিযোগটি গুরুত্বের সাথে নিচ্ছি। আপনার order ID আর নাম বলবেন?

**৪. কাস্টমারঃ** আমার নাম সালমা বেগম, order ID হচ্ছে DZ-৪৫৬৭৮৯০১২। তিনটাই একসাথে অর্ডার দিয়েছিলাম, তাহলে একসাথে আসার কথা না?

**৫. এজেন্টঃ** ম্যাম, ধন্যবাদ। আমি আপনার order details চেক করে বুঝিয়ে বলছি। বিস্তারিত বলছি — Daraz একটি marketplace, এখানে একই order-এ বিভিন্ন seller-এর product থাকতে পারে। আপনার চপিং বোর্ড আর মসলার জার সেট একজন seller "Kitchen World BD" থেকে এসেছে, কিন্তু ব্লেন্ডারটি সম্পূর্ণ আলাদা একজন seller "Home Appliance Hub"-এর product। তাই আলাদা আলাদা shipment-এ আসছে।

**৬. কাস্টমারঃ** ও আচ্ছা! আমি তো ভেবেছিলাম সব একই জায়গা থেকে আসে। তাহলে ব্লেন্ডারটা কবে আসবে আপু?

**৭. এজেন্টঃ** ম্যাম, আমি দেখছি ব্লেন্ডারের seller এখনো product টি dispatch করেনি। Seller-কে dispatch করতে সাধারণত ২ কর্মদিবস সময় দেওয়া হয়, আর আজকে শেষ দিন।

**৮. কাস্টমারঃ** মানে আজকে dispatch না করলে কী হবে? আমি কি শুধু ব্লেন্ডারটা cancel করে দিতে পারবো?

**৯. এজেন্টঃ** জ্বী ম্যাম, seller যদি নির্ধারিত সময়ের মধ্যে dispatch না করে, তাহলে system automatically সেই item cancel করে দেবে এবং আপনি সেই item-এর full refund পাবেন।

**১০. কাস্টমারঃ** আপু, আমি আসলে ব্লেন্ডারটা দরকার, cancel করতে চাই না। কিন্তু seller-কে কি একটু তাগাদা দেওয়া যায়?

**১১. এজেন্টঃ** ম্যাম, আমি seller-কে একটি urgent dispatch reminder পাঠিয়ে দিচ্ছি। এছাড়া আপনি চাইলে Daraz app-এ seller-কে সরাসরি message করতে পারেন।

**১২. কাস্টমারঃ** কিভাবে message করবো আপু? আমি তো এত কিছু জানি না app-এ।

**১৩. এজেন্টঃ** ম্যাম, খুব সহজ। App-এ "My Orders" section-এ যান, এই order-এ click করুন, তারপর ব্লেন্ডারের item-এর নিচে "Chat with Seller" button দেখতে পাবেন।

**১৪. কাস্টমারঃ** আচ্ছা পেয়েছি আপু। আর একটা কথা, যে দুইটা এসেছে সেগুলোর quality ভালো আছে, কিন্তু চপিং বোর্ডের সাইজ ছবিতে যেটা দেখেছিলাম তার চেয়ে ছোট মনে হচ্ছে।

**১৫. এজেন্টঃ** ম্যাম, product page-এ dimensions লেখা থাকে, সেটা মিলিয়ে দেখুন। যদি product description-এর সাথে না মেলে, তাহলে আপনি ৭ দিনের মধ্যে return request দিতে পারবেন।

**১৬. কাস্টমারঃ** আচ্ছা আপু, পরে মেপে দেখবো। ব্লেন্ডারটা dispatch হলে কতদিনের মধ্যে পাবো?

**১৭. এজেন্টঃ** ম্যাম, dispatch হলে ঢাকার মধ্যে সাধারণত ২ থেকে ৩ দিনের মধ্যে delivery হয়। Seller-এর location-এর উপরও নির্ভর করে।

**১৮. কাস্টমারঃ** আচ্ছা। আর ভবিষ্যতে যদি নিশ্চিত হতে চাই সব জিনিস একসাথে আসবে, তাহলে কী করবো আপু?

**১৯. এজেন্টঃ** ম্যাম, একই seller-এর product কিনলে সাধারণত একই shipment-এ আসে। Order করার সময় প্রতিটা item-এর নিচে seller-এর নাম দেখবেন, সব same seller হলে একসাথে পাবেন।

**২০. কাস্টমারঃ** বুঝেছি আপু, এটা মাথায় রাখবো। আচ্ছা, ব্লেন্ডারের বিষয়ে কি পরে আবার call করতে পারি?

**২১. এজেন্টঃ** জ্বী ম্যাম, যেকোনো সময় call করতে পারবেন। আর app-এ order track করলেও real-time update পাবেন, dispatch হলে notification আসবে।

**২২. কাস্টমারঃ** ঠিক আছে আপু। অনেক ধন্যবাদ নুসরাত আপু, সুন্দর করে বুঝিয়ে দিলেন।

**২৩. এজেন্টঃ** আপনাকেও ধন্যবাদ সালমা ম্যাম। Daraz-এ কেনাকাটা উপভোগ করুন, শুভ দিন কাটুক।

---

## সিনারিও ৫ঃ Fragile আইটেম বিনা packaging-এ ডেলিভারি

> একজন কাস্টমার ceramic dinner set অর্ডার করেছেন। Parcel-এ কোনো bubble wrap বা fragile label ছিল না, ফলে কয়েকটি plate ভেঙে গেছে।

**১. এজেন্টঃ** Daraz customer care থেকে সাবরিনা বলছি। আপনার সমস্যাটি বলুন স্যার, আমি order details দেখে যথাযথভাবে সাহায্য করছি।

**২. কাস্টমারঃ** আপু, আমি ceramic dinner set অর্ডার করেছিলাম। Parcel খুলে দেখি packaging প্রায় ছিলই না, কয়েকটি plate ভেঙে গেছে।

**৩. এজেন্টঃ** আপনার অসুবিধার জন্য দুঃখিত স্যার। Damaged item claim করার জন্য আপনার order ID এবং product-এর নামটি বলবেন?

**৪. কাস্টমারঃ** Order ID DZ-৮৯০১২৩৪৫৬। Product ছিল twelve-piece ceramic dinner set, আর delivery পেয়েছি আজ দুপুরে।

**৫. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered mobile number এবং parcel-এর বাইরের packaging কেমন ছিল, সেটি একটু জানাবেন?

**৬. কাস্টমারঃ** আমার নম্বর ০১৭১২৩৪৫৬৭৮। শুধু পাতলা carton ছিল, কোনো bubble wrap, foam বা Fragile sticker কিছুই ছিল না।

**৭. এজেন্টঃ** বুঝতে পেরেছি স্যার। বিস্তারিত বুঝিয়ে বলছি, fragile product-এর ক্ষেত্রে seller-এর নিরাপদ packaging ব্যবহার করা উচিত। Claim যাচাইয়ের জন্য product, box label এবং damaged অংশের ছবি দরকার হবে।

**৮. কাস্টমারঃ** আমি ছবি তুলেছি। মোট চারটি plate ভেঙেছে, আর দুইটি plate-এ বড় crack আছে। বাকি জিনিসগুলোও ব্যবহার করতে ভয় লাগছে।

**৯. এজেন্টঃ** স্যার, অনুগ্রহ করে ভাঙা ceramic অংশগুলো আলাদা করে নিরাপদ স্থানে রাখবেন। আমি এখন আপনার order-এর জন্য damaged delivery return request তৈরি করছি।

**১০. কাস্টমারঃ** আমি পুরো set-এর replacement চাই। শুধু চারটি plate বদলালে design আর color একই থাকবে কিনা নিশ্চিত নই।

**১১. এজেন্টঃ** আপনার replacement preference request-এ লিখে দিলাম স্যার। Seller-এর কাছে একই set থাকলে complete replacement-এর জন্য পাঠানো হবে।

**১২. কাস্টমারঃ** Seller যদি replacement না দেয়, তাহলে কি পুরো টাকা refund হবে? আমি অসম্পূর্ণ dinner set রাখতে চাই না।

**১৩. এজেন্টঃ** জ্বী স্যার, stock না থাকলে অথবা replacement সম্ভব না হলে policy অনুযায়ী full refund option review করা হবে।

**১৪. কাস্টমারঃ** Return pickup-এর আগে কি আমাকে damaged item আবার pack করতে হবে? ভাঙা জিনিস ঠিকভাবে pack করা কঠিন।

**১৫. এজেন্টঃ** স্যার, শক্ত carton ব্যবহার করে প্রতিটি ভাঙা অংশ কাগজ বা bubble wrap দিয়ে আলাদা করবেন। বাইরে Fragile এবং Handle with care লিখে রাখবেন।

**১৬. কাস্টমারঃ** Pickup কি আমার বাসা থেকে হবে, নাকি আমাকে courier office-এ নিয়ে যেতে হবে?

**১৭. এজেন্টঃ** আপনার ঠিকানা pickup coverage-এর মধ্যে থাকলে courier representative বাসা থেকেই item সংগ্রহ করবে। Schedule হলে app এবং SMS-এ সময় জানানো হবে।

**১৮. কাস্টমারঃ** Seller packaging ঠিক ছিল বললে কি আমার claim বাতিল হয়ে যাবে? আমি তো delivery সময়েই damage দেখেছি।

**১৯. এজেন্টঃ** না স্যার, আপনার ছবি, packaging condition এবং delivery record একসঙ্গে review করা হবে। Seller-এর বক্তব্য একা claim বাতিলের কারণ নয়।

**২০. কাস্টমারঃ** ঠিক আছে আপু। Return request-এর reference number এবং পরবর্তী update কখন পাবো?

**২১. এজেন্টঃ** আপনার ticket number DZ-RET-২০২৬-০০৫। সাধারণত ২৪ থেকে ৭২ ঘণ্টার মধ্যে pickup update এবং এরপর inspection result জানানো হয়।

**২২. কাস্টমারঃ** বুঝেছি সাবরিনা আপু। আমি এখন ছবি upload করে item নিরাপদে রাখছি, ধন্যবাদ।

**২৩. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। Pickup না হওয়া পর্যন্ত broken ceramic শিশুদের কাছ থেকে দূরে রাখবেন। Daraz team আপনার request follow করবে।

---

## সিনারিও ৬ঃ Delivery rider COD amount-এর বাইরে অতিরিক্ত টাকা চাইছে

> একজন কাস্টমার COD order গ্রহণের সময় rider-এর অতিরিক্ত টাকা দাবি নিয়ে কল করেন। App-এ কোনো additional charge না থাকলেও rider delivery fee দাবি করেছে।

**১. কাস্টমারঃ** Daraz থেকে parcel এসেছে, কিন্তু rider app-এ দেখানো টাকার চেয়ে ২০০ টাকা বেশি চাইছে। এই charge কি বৈধ?

**২. এজেন্টঃ** Daraz customer care থেকে তানিম বলছি। বিষয়টি যাচাই করছি স্যার। আপনার order ID এবং app-এ দেখানো payable amount বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-৩৪৫৬৭৮৯০১। App-এ amount ৮৫০ টাকা, কিন্তু rider মোট ১,০৫০ টাকা চাইছে।

**৪. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered number এবং rider অতিরিক্ত ২০০ টাকার কারণ হিসেবে কী বলেছেন?

**৫. কাস্টমারঃ** আমার নম্বর ০১৯১২৩৪৫৬৭৮। তিনি বলেছেন আমার এলাকা নাকি special delivery zone, তাই extra charge দিতে হবে।

**৬. এজেন্টঃ** আমি order summary চেক করছি স্যার। সেখানে product price এবং delivery fee মিলিয়ে payable amount ৮৫০ টাকা দেখাচ্ছে, কোনো special charge নেই।

**৭. কাস্টমারঃ** তাহলে আমি কি শুধু ৮৫০ টাকা দিয়ে parcel নিতে পারবো? Rider বলছে অতিরিক্ত টাকা না দিলে delivery cancel করবে।

**৮. এজেন্টঃ** জ্বী স্যার, app-এ প্রদর্শিত official amount-এর বাইরে payment করবেন না। আমি এখন rider supervisor-এর কাছে বিষয়টি escalate করছি।

**৯. কাস্টমারঃ** Rider এখনো gate-এর সামনে আছে। আমি তাকে অপেক্ষা করতে বলেছি, কিন্তু সে খুব রাগারাগি করছে।

**১০. এজেন্টঃ** স্যার, আপনি শান্ত থাকুন এবং কোনো তর্কে যাবেন না। আমি delivery record দেখে rider-এর assigned route ও payable instruction verify করছি।

**১১. কাস্টমারঃ** আমি cash নিয়ে দাঁড়িয়ে আছি। যদি official amount দিয়ে parcel নিই, receipt কীভাবে নিশ্চিত করবো?

**১২. এজেন্টঃ** স্যার, ৮৫০ টাকা দেওয়ার পর delivery confirmation অথবা payment receipt চাইবেন। App-এ order status delivered হওয়ার screenshot-ও রেখে দেবেন।

**১৩. কাস্টমারঃ** Supervisor কি rider-এর সঙ্গে কথা বলেছেন? আমি চাই সমস্যাটি এখনই শেষ হোক।

**১৪. এজেন্টঃ** জ্বী স্যার, supervisor rider-কে নিশ্চিত করেছেন যে আপনার order-এ কোনো additional fee নেই। Rider-কে শুধু ৮৫০ টাকা গ্রহণ করে delivery করতে বলা হয়েছে।

**১৫. কাস্টমারঃ** ভালো। কিন্তু এই rider যদি অন্য customer-এর কাছ থেকেও extra charge নেয়, তাহলে কি ব্যবস্থা হবে?

**১৬. এজেন্টঃ** আপনার অভিযোগটি delivery conduct complaint হিসেবে log করছি স্যার। Operations team rider-এর অন্যান্য delivery record এবং supervisor report review করবে।

**১৭. কাস্টমারঃ** আমি extra টাকা দিইনি, তবে rider-এর phone number আর vehicle plate লিখে রেখেছি। এগুলো কি complaint-এ যোগ করবেন?

**১৮. এজেন্টঃ** অবশ্যই স্যার। Rider-এর contact number, vehicle information এবং আপনার বক্তব্য তদন্তে সহায়তা করবে। এগুলো ticket details-এ যুক্ত করছি।

**১৯. কাস্টমারঃ** Order cancel হলে কি আমার account-এ কোনো penalty আসবে? Cancel করার কথা তো আমি বলিনি।

**২০. এজেন্টঃ** না স্যার, আপনি official amount দিতে প্রস্তুত থাকলে customer fault হিসেবে cancellation হওয়ার কথা নয়। প্রয়োজনে আমরা delivery attempt review করবো।

**২১. কাস্টমারঃ** Complaint reference number দিন। Rider এখন ৮৫০ টাকা নিয়ে parcel দিচ্ছে।

**২২. এজেন্টঃ** আপনার complaint reference DZ-DEL-২০২৬-০০৬। Parcel নেওয়ার পর package condition এবং receipt যাচাই করে তারপর delivery confirmation দিন।

**২৩. কাস্টমারঃ** ঠিক আছে তানিম ভাই। Official amount ছাড়া টাকা না দেওয়ার বিষয়টি পরিষ্কার করে বলার জন্য ধন্যবাদ।

**২৪. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। ভবিষ্যতে app-এর payable amount মিলিয়ে payment করবেন এবং সন্দেহজনক দাবি হলে সঙ্গে সঙ্গে আমাদের জানাবেন।

---

## সিনারিও ৭ঃ Sorting center-এ সাত দিন ধরে parcel আটকে আছে

> একজন শিক্ষার্থী একটি calculator অর্ডার করেছেন, কিন্তু tracking status সাত দিন ধরে sorting center-এ অপরিবর্তিত। পরীক্ষার আগে product না পাওয়ায় তিনি জরুরি update চান।

**১. এজেন্টঃ** Daraz customer care থেকে ফারিয়া বলছি। আপনার delivery concern শুনছি স্যার। Order ID-টি বলবেন, আমি tracking details চেক করছি।

**২. কাস্টমারঃ** আপু, আমার calculator parcel সাত দিন ধরে sorting center-এ আটকে আছে। সামনে পরীক্ষা, তাই বিষয়টি নিয়ে খুব চিন্তায় আছি।

**৩. এজেন্টঃ** আপনার উদ্বেগটি বুঝতে পারছি স্যার। Order ID, product-এর নাম এবং expected delivery date-টি জানাবেন?

**৪. কাস্টমারঃ** Order ID DZ-৬৭৮৯০১২৩৪। Product scientific calculator, আর expected delivery ছিল গত শুক্রবার।

**৫. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered mobile number নিশ্চিত করবেন? তারপর আমি courier movement এবং latest scan event দেখছি।

**৬. কাস্টমারঃ** নম্বর ০১৬১২৩৪৫৬৭৮। Tracking-এ শুধু “At Sorting Center” লেখা, সাত দিনেও নতুন কোনো update নেই।

**৭. এজেন্টঃ** স্যার, আমি দেখতে পাচ্ছি parcelটি চট্টগ্রাম sorting center-এ আটকে আছে। বিস্তারিত বুঝিয়ে বলছি, কখনো shipment label scan বা route allocation-এ সমস্যা হলে parcel physical movement করলেও online status update হয় না। তবে সাত দিন update না থাকা স্বাভাবিক নয়, তাই আমি courier investigation request করছি।

**৮. কাস্টমারঃ** আমি ঢাকায় থাকি, চট্টগ্রামে parcel কেন গেল? Seller কি ভুল route-এ পাঠিয়েছে?

**৯. এজেন্টঃ** স্যার, seller-এর dispatch location খুলনায় এবং courier network অনুযায়ী regional hub হয়ে parcel ঢাকায় আসার কথা। বর্তমানে route deviation হয়েছে কিনা operations team যাচাই করবে।

**১০. কাস্টমারঃ** আমার পরীক্ষা তিন দিন পরে। এই parcel সময়মতো না এলে calculator ছাড়া সমস্যায় পড়বো।

**১১. এজেন্টঃ** আপনার urgency বুঝতে পারছি স্যার। আমি ticket-এ exam-related delivery note যোগ করছি এবং courier team-কে priority trace request পাঠাচ্ছি।

**১২. কাস্টমারঃ** Trace request-এর result কখন পাবো? আমি কি parallelভাবে অন্য calculator কিনে ফেলবো?

**১৩. এজেন্টঃ** স্যার, courier সাধারণত ২৪ থেকে ৪৮ ঘণ্টার মধ্যে trace update দেয়। আপনার পরীক্ষা জরুরি হলে backup ব্যবস্থা রাখা বাস্তবসম্মত, তবে এই order-এর update আমরা জানাবো।

**১৪. কাস্টমারঃ** যদি parcel হারিয়ে যায়, তাহলে কি refund পেতে আলাদা claim করতে হবে?

**১৫. এজেন্টঃ** না স্যার, investigation-এ parcel lost প্রমাণিত হলে delivery failure case অনুযায়ী cancellation এবং refund process করা হবে।

**১৬. কাস্টমারঃ** আমি prepaid payment করেছি। Refund হলে কি একই payment method-এ টাকা আসবে?

**১৭. এজেন্টঃ** স্যার, prepaid order-এর refund সাধারণত original payment method বা available refund option অনুযায়ী process হয়। Finance review শেষ হলে নির্দিষ্ট timeline জানানো হবে।

**১৮. কাস্টমারঃ** Sorting center থেকে কি আমি নিজে parcel collect করতে পারবো? এতে হয়তো সময় বাঁচবে।

**১৯. এজেন্টঃ** দুঃখিত স্যার, security এবং route policy-এর কারণে customer সাধারণত sorting center থেকে parcel collect করতে পারেন না। Courier delivery route-এই parcel পাঠাবে।

**২০. কাস্টমারঃ** ঠিক আছে। আমার investigation ticket number এবং next update-এর সময়টা বলবেন?

**২১. এজেন্টঃ** আপনার investigation reference DZ-TRC-২০২৬-০০৭। আগামী ৪৮ ঘণ্টার মধ্যে SMS, app notification অথবা phone call-এর মাধ্যমে update দেওয়া হবে।

**২২. কাস্টমারঃ** বুঝেছি ফারিয়া আপু। আমার exam-এর বিষয়টি ticket-এ লিখে রাখার জন্য ধন্যবাদ।

**২৩. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। নতুন update না আসা পর্যন্ত একই order নিয়ে duplicate complaint না করে এই reference ব্যবহার করবেন।

---

## সিনারিও ৮ঃ Delivery attempt ব্যর্থ দেখাচ্ছে, কিন্তু customer সারাদিন বাসায় ছিলেন

> একজন কাস্টমার tracking-এ “Customer unavailable” status দেখে কল করেন। তিনি জানান, সারা দিন বাসায় থাকলেও rider কোনো call বা visit করেননি।

**১. কাস্টমারঃ** আমার parcel-এ “Customer unavailable” লেখা হয়েছে, কিন্তু আমি সারাদিন বাসায় ছিলাম। Rider আমাকে call-ও করেনি।

**২. এজেন্টঃ** Daraz customer care থেকে নুসরাত বলছি। আপনার অভিযোগটি যাচাই করছি ম্যাম। Order ID এবং delivery date বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-১২৩৪৫৬৭৮৯। আজ দুপুরে delivery attempt দেখাচ্ছে, কিন্তু কেউ বাসায় আসেনি।

**৪. এজেন্টঃ** ধন্যবাদ ম্যাম। আপনার registered mobile number এবং delivery address-এর area-টি নিশ্চিত করবেন?

**৫. কাস্টমারঃ** নম্বর ০১৮১২৩৪৫৬৭৮। Address হলো বসুন্ধরা আবাসিক এলাকা, block C। আমি সকাল থেকে বাসায় ছিলাম।

**৬. এজেন্টঃ** তথ্যগুলো মিলে গেছে ম্যাম। আমি delivery log, rider call record এবং attempt remark চেক করছি। একটু সময় দেবেন?

**৭. কাস্টমারঃ** জ্বী, দেখুন। Parcel-টি আমার মায়ের medicine organizer, তাই আজই পাওয়ার কথা ছিল।

**৮. এজেন্টঃ** ধন্যবাদ অপেক্ষা করার জন্য ম্যাম। System-এ rider “customer unavailable” লিখেছে, কিন্তু call attempt-এর কোনো record নেই। আমি বিষয়টি false attempt হিসেবে report করছি।

**৯. কাস্টমারঃ** তাহলে rider কি না এসেই status update করেছে? এটা হলে তো আমার delivery আবার পিছিয়ে যাবে।

**১০. এজেন্টঃ** ম্যাম, আপনার order-এ reattempt request দিচ্ছি। Operations team rider-কে আপনার address-এ পুনরায় পাঠাবে এবং supervisor verification রাখবে।

**১১. কাস্টমারঃ** আজ রাতেই কি আবার delivery হতে পারে? আমার মায়ের জিনিসটি জরুরি, কাল পর্যন্ত অপেক্ষা করা কঠিন।

**১২. এজেন্টঃ** ম্যাম, same-day reattempt courier availability-এর উপর নির্ভর করে। আমি urgent note দিচ্ছি, তবে নিশ্চিত সময় courier team response না পাওয়া পর্যন্ত বলতে পারছি না।

**১৩. কাস্টমারঃ** Rider আসার আগে কি আমাকে call করতে বলা যাবে? Unknown number হলে আমার মা phone ধরতে চান না।

**১৪. এজেন্টঃ** অবশ্যই ম্যাম। Delivery instruction-এ “arrival-এর আগে customer-কে call করতে হবে” লিখে দিচ্ছি এবং আপনার preferred contact number confirm করছি।

**১৫. কাস্টমারঃ** যদি rider আবার না আসে, তাহলে কি আমি pickup point থেকে parcel নিতে পারবো?

**১৬. এজেন্টঃ** ম্যাম, কিছু shipment-এ pickup option থাকে, তবে আপনার order-এ বর্তমানে home delivery selected। Courier confirmation ছাড়া pickup point-এ যাওয়া ঠিক হবে না।

**১৭. কাস্টমারঃ** এই false attempt-এর জন্য কি delivery charge ফেরত পাওয়া যায়? আমার তো service পাইনি।

**১৮. এজেন্টঃ** ম্যাম, delivery charge refund বা compensation policy order review-এর পর নির্ধারিত হয়। আমি আপনার inconvenience note-এ লিখে রাখছি, operations team বিষয়টি বিবেচনা করবে।

**১৯. কাস্টমারঃ** Rider-এর বিরুদ্ধে complaint করলে কি সে পরে ইচ্ছা করে delivery delay করবে?

**২০. এজেন্টঃ** না ম্যাম, complaint confidentialভাবে review করা হয়। আপনার future delivery যাতে নিরপেক্ষভাবে হয়, সে জন্য account note-এ শুধু verification instruction যোগ করছি।

**২১. কাস্টমারঃ** Reattempt request-এর reference number দিন। আমি app-এ tracking দেখতে চাই।

**২২. এজেন্টঃ** আপনার reference DZ-REA-২০২৬-০০৮। নতুন attempt schedule হলে app notification এবং SMS আসবে; rider call না করলে আবার এই reference ব্যবহার করবেন।

**২৩. কাস্টমারঃ** ঠিক আছে নুসরাত আপু। আজকের বিষয়টি গুরুত্ব দিয়ে দেখার জন্য ধন্যবাদ।

**২৪. এজেন্টঃ** আপনাকেও ধন্যবাদ ম্যাম। Delivery-এর সময় phone কাছে রাখবেন এবং parcel গ্রহণের আগে order details মিলিয়ে নেবেন।

---

## সিনারিও ৯ঃ অনুমতি ছাড়াই প্রতিবেশীর কাছে parcel রেখে গেছে

> একজন customer বাড়িতে না থাকায় delivery rider কোনো confirmation ছাড়াই parcel পাশের ফ্ল্যাটের প্রতিবেশীর কাছে রেখে delivered mark করেছেন। Customer security ও privacy নিয়ে উদ্বিগ্ন।

**১. এজেন্টঃ** Daraz customer care থেকে ফারিয়া বলছি। আপনার delivery concern-টি বলুন ম্যাম, আমি order details দেখে সাহায্য করছি।

**২. কাস্টমারঃ** আপু, tracking-এ parcel delivered দেখাচ্ছে, কিন্তু আমি তখন বাসায় ছিলাম না। পরে জানতে পারলাম rider আমার অনুমতি ছাড়াই পাশের ফ্ল্যাটে রেখে গেছে।

**৩. এজেন্টঃ** ম্যাম, আপনার অনুমতি ছাড়া অন্য কারো কাছে parcel দেওয়া নিয়ে দুঃখিত। Order ID এবং delivery address-এর building information বলবেন?

**৪. কাস্টমারঃ** Order ID DZ-৯০১২৩৪৫৬৭। আমি ধানমণ্ডির একটি apartment building-এ থাকি, parcel আমার ৬B ফ্ল্যাটের।

**৫. এজেন্টঃ** ধন্যবাদ ম্যাম। আপনার registered number এবং delivery proof-এ receiver হিসেবে কার নাম লেখা আছে, সেটি জানাবেন?

**৬. কাস্টমারঃ** আমার নম্বর ০১৭৮১২৩৪৫৬৭। Proof-এ পাশের ফ্ল্যাটের security guard-এর নাম লেখা, কিন্তু আমি তাকে receive করার permission দিইনি।

**৭. এজেন্টঃ** তথ্য যাচাই হয়েছে ম্যাম। আমি দেখতে পাচ্ছি rider customer unavailable হওয়ার পর building security desk-এ parcel রেখে delivery confirm করেছেন। এই process যথাযথভাবে follow হয়েছে কিনা review করছি।

**৮. কাস্টমারঃ** Security desk-এ parcel থাকলে যে কেউ নিয়ে যেতে পারে। আমি এখন অফিসে আছি, রাতে গিয়ে নিলে কি parcel safe থাকবে?

**৯. এজেন্টঃ** ম্যাম, আমি delivery supervisor-কে contact করে parcelটি secureভাবে রাখার নির্দেশ দিচ্ছি। আপনি চাইলে trusted family member-কে authorization দিয়ে collect করাতে পারেন।

**১০. কাস্টমারঃ** আমি আমার বোনকে পাঠাবো। তার নাম নাবিলা, কিন্তু security যেন ভুল কাউকে parcel না দেয়।

**১১. এজেন্টঃ** ম্যাম, আপনার authorization note-এ নাবিলা নামটি যুক্ত করছি। তিনি collection-এর সময় order ID এবং আপনার registered number-এর শেষ চার digit দেখাবেন।

**১২. কাস্টমারঃ** Rider কি আমাকে call করার চেষ্টা করেছিল? আমি কোনো missed call পাইনি।

**১৩. এজেন্টঃ** ম্যাম, call log-এ কোনো successful call record নেই। শুধু delivery attempt remark আছে, তাই rider-এর handling নিয়ে আলাদা complaint log করছি।

**১৪. কাস্টমারঃ** এই ধরনের delivery আমার একদম পছন্দ নয়। ভবিষ্যতে কি নির্দিষ্ট কারো কাছে দেওয়ার instruction দেওয়া যায়?

**১৫. এজেন্টঃ** জ্বী ম্যাম, Address Book-এর delivery instruction-এ authorized receiver-এর নাম লিখতে পারেন। তবে rider availability অনুযায়ী instruction সবসময় guarantee করা যায় না।

**১৬. কাস্টমারঃ** আমি চাই rider আগে call করুক এবং কেউ না থাকলে delivery attempt না করুক। এটা কি account note হিসেবে রাখা যাবে?

**১৭. এজেন্টঃ** অবশ্যই ম্যাম। আপনার account-এ “Call before delivery, do not leave with neighbor without approval” instruction যুক্ত করছি।

**১৮. কাস্টমারঃ** Parcel খুলে গেলে বা product missing থাকলে কি আমি return request দিতে পারবো?

**১৯. এজেন্টঃ** ম্যাম, parcel গ্রহণের পর packaging এবং contents-এর ছবি রাখবেন। Tampering, missing item বা damage থাকলে evidenceসহ return request করা যাবে।

**২০. কাস্টমারঃ** Complaint reference এবং authorized collection-এর update কখন পাবো?

**২১. এজেন্টঃ** আপনার complaint reference DZ-SEC-২০২৬-০০৯। Security confirmation পাওয়ার পর আজ সন্ধ্যার মধ্যে app notification পাঠানো হবে।

**২২. কাস্টমারঃ** ঠিক আছে ফারিয়া আপু। আমি বোনকে পাঠাচ্ছি এবং receipt না পাওয়া পর্যন্ত collection confirm করবো না।

**২৩. এজেন্টঃ** সেটিই সঠিক হবে ম্যাম। Authorized person ছাড়া কাউকে parcel দেবেন না এবং কোনো সমস্যা হলে reference নম্বরটি ব্যবহার করবেন।

---

## সিনারিও ১০ঃ অন্য customer-এর parcel এসেছে, নিজের order পাওয়া যায়নি

> একজন customer একটি phone charger অর্ডার করেছিলেন, কিন্তু delivery-তে তার নামে অন্য product এসেছে। নিজের parcel missing হওয়ায় তিনি দ্রুত exchange ও investigation চান।

**১. কাস্টমারঃ** আমার order ছিল phone charger, কিন্তু delivery-তে অন্য একজনের নামের parcel এসেছে। আমার নিজের product এখনো পাইনি।

**২. এজেন্টঃ** Daraz customer care থেকে আরিফ বলছি। এই ভুল delivery-এর জন্য দুঃখিত স্যার। আপনার order ID এবং received parcel-এর label details বলবেন?

**৩. কাস্টমারঃ** আমার order ID DZ-৫৬৭৮৯০১২৩। Parcel-এ নাম লেখা আছে মেহেদী হাসান, আর ভিতরে kitchen mixer-এর box রয়েছে।

**৪. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered mobile number এবং আপনার আসল order-এ product name ও seller-এর নামটি নিশ্চিত করবেন?

**৫. কাস্টমারঃ** নম্বর ০১৮৯৮৭৬৫৪৩২। Product Anker-type charger, seller-এর নাম Tech Corner BD।

**৬. এজেন্টঃ** তথ্যগুলো মিলে গেছে স্যার। Received parcel-এর barcode এবং আপনার order shipment record মিলিয়ে দেখছি। অনুগ্রহ করে parcel label-এর ছবি সংরক্ষণ করবেন।

**৭. কাস্টমারঃ** Rider চলে যাওয়ার আগে আমি label-এর ছবি নিয়েছি। কিন্তু এখন অন্যের parcel আমার কাছে রাখা কি নিরাপদ?

**৮. এজেন্টঃ** স্যার, parcelটি ব্যবহার বা খোলা থেকে বিরত থাকবেন। আমি reverse pickup এবং correct parcel trace করার জন্য logistics team-এ request পাঠাচ্ছি।

**৯. কাস্টমারঃ** আমি box খুলেছি, কারণ বাইরে charger লেখা ছিল না। ভিতরে mixer দেখে সঙ্গে সঙ্গে বন্ধ করেছি, কোনো জিনিস ব্যবহার করিনি।

**১০. এজেন্টঃ** বুঝতে পেরেছি স্যার। যেহেতু item ব্যবহার করেননি, box এবং accessories আগের অবস্থায় রাখবেন। Pickup agent এসে parcelটি collect করবে।

**১১. কাস্টমারঃ** আমার charger কি নতুন করে পাঠানো হবে, নাকি order cancel হয়ে যাবে?

**১২. এজেন্টঃ** স্যার, আপনার original shipment কোথায় আছে তা trace করা হবে। পাওয়া গেলে correct delivery reattempt করা হবে, আর lost হলে refund বা replacement option দেওয়া হবে।

**১৩. কাস্টমারঃ** Tracking-এ আমার order এখনো out for delivery দেখাচ্ছে। তাহলে rider কেন অন্য parcel দিল?

**১৪. এজেন্টঃ** স্যার, warehouse sorting বা barcode scanning-এর সময় shipment swap হয়েছে বলে মনে হচ্ছে। Courier operations team rider route এবং package scan history review করবে।

**১৫. কাস্টমারঃ** আমি কি ওই অন্য customer-এর নাম বা phone number জানতে পারবো, যাতে নিজে যোগাযোগ করি?

**১৬. এজেন্টঃ** দুঃখিত স্যার, privacy policy-এর কারণে অন্য customer-এর personal information দেওয়া যাবে না। Courier team দুইটি parcel exchange coordinate করবে।

**১৭. কাস্টমারঃ** Pickup কবে হবে? আমি সারাদিন অফিসে থাকি, তাই সময়টা আগে জানা দরকার।

**১৮. এজেন্টঃ** স্যার, আপনার delivery preference অনুযায়ী pickup-এর আগে call instruction দিচ্ছি। সাধারণত ২৪ থেকে ৪৮ ঘণ্টার মধ্যে schedule confirmation আসে।

**১৯. কাস্টমারঃ** যদি pickup agent অন্য parcel নিতে না আসে, তাহলে কি আমাকে আবার call করতে হবে?

**২০. এজেন্টঃ** স্যার, reference number দিয়ে app Help Center-এ status দেখা যাবে। নির্ধারিত সময় পার হলে একই ticket-এ follow-up করবেন, নতুন complaint দরকার হবে না।

**২১. কাস্টমারঃ** আমার charger-এর prepaid payment করা হয়েছে। Refund হলে আমি কতদিন অপেক্ষা করবো?

**২২. এজেন্টঃ** স্যার, parcel loss বা cancellation confirm হলে payment method অনুযায়ী refund initiate হবে। Finance processing time notification-এ জানানো হবে।

**২৩. কাস্টমারঃ** Reference number এবং pickup request-এর details দিন, আমি save করে রাখছি।

**২৪. এজেন্টঃ** আপনার shipment mismatch reference DZ-MIS-২০২৬-০১০। Mixer box নিরাপদে রাখবেন এবং pickup-এর সময় handover receipt সংগ্রহ করবেন।

**২৫. কাস্টমারঃ** ঠিক আছে আরিফ ভাই। অন্যের parcel নিয়ে কী করতে হবে সেটা পরিষ্কার করে বলার জন্য ধন্যবাদ।

**২৬. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। আপনার correct charger shipment trace করে update দেওয়া হবে। ভালো থাকবেন।

---

## সিনারিও ১১ঃ সকাল থেকে “Out for delivery”, রাত হয়ে গেলেও parcel আসেনি

> একজন customer জরুরি office document folder অর্ডার করেছেন। Tracking সকাল থেকে out for delivery দেখাচ্ছে, কিন্তু রাত হয়ে গেলেও rider আসেননি এবং কোনো call করেননি।

**১. এজেন্টঃ** Daraz customer care থেকে সাবরিনা বলছি। Delivery status নিয়ে কী সমস্যা হচ্ছে বলুন স্যার, আমি এখনই check করছি।

**২. কাস্টমারঃ** সকাল ৯টা থেকে tracking-এ out for delivery দেখাচ্ছে। এখন রাত ৮টা, কিন্তু rider আসেনি এবং কোনো call-ও করেনি।

**৩. এজেন্টঃ** দেরির জন্য দুঃখিত স্যার। আপনার order ID এবং আজকের expected delivery time window-টি বলবেন?

**৪. কাস্টমারঃ** Order ID DZ-২৪৬৮০১৩৫৭। App-এ আজ delivery দেখাচ্ছিল, productটা office-এর জন্য document folder।

**৫. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered number এবং delivery area-টি নিশ্চিত করবেন, যাতে rider route status দেখা যায়?

**৬. কাস্টমারঃ** নম্বর ০১৫৯৮৭৬৫৪৩২। আমি মতিঝিলে থাকি, কিন্তু সন্ধ্যার পর building gate বন্ধ হয়ে যায়।

**৭. এজেন্টঃ** স্যার, route record-এ parcelটি এখনো rider-এর possession-এ আছে। বিস্তারিত বুঝিয়ে বলছি, “Out for delivery” status সাধারণত route assignment বোঝায়, নির্দিষ্ট arrival time নয়। Traffic, route load বা address access issue হলে একই দিনে delivery পিছিয়ে যেতে পারে, তবে customer-কে update দেওয়া উচিত ছিল।

**৮. কাস্টমারঃ** তাহলে আজ কি delivery হবে? আমি আর কতক্ষণ বাসায় অপেক্ষা করবো?

**৯. এজেন্টঃ** স্যার, আমি rider supervisor-এর কাছে current route position এবং remaining stops জানতে request পাঠাচ্ছি। Confirmation না পাওয়া পর্যন্ত নির্দিষ্ট সময়ের প্রতিশ্রুতি দিতে চাই না।

**১০. কাস্টমারঃ** কাল সকালে office presentation আছে। আজ না পেলে productটির কোনো কাজে আসবে না।

**১১. এজেন্টঃ** আপনার deadline বুঝতে পারছি স্যার। Ticket-এ morning-use requirement লিখছি এবং আজকের delivery attempt priority review-এর জন্য পাঠাচ্ছি।

**১২. কাস্টমারঃ** Rider যদি রাত ১০টার পরে আসে, তখন gate বন্ধ থাকবে। অন্য কোনো delivery instruction দিতে পারবো?

**১৩. এজেন্টঃ** জ্বী স্যার, gate security desk-এ authorized handover করা যাবে কিনা আপনি আগে নিশ্চিত করুন। আপনার অনুমতি ছাড়া আমরা security desk-এ parcel রাখতে বলবো না।

**১৪. কাস্টমারঃ** আমি building guard-কে receive করতে বলতে পারি, তবে rider অবশ্যই আগে আমাকে call করবে।

**১৫. এজেন্টঃ** আপনার instruction update করছি: arrival-এর আগে registered number-এ call করতে হবে এবং customer confirmation ছাড়া parcel leave করা যাবে না।

**১৬. কাস্টমারঃ** যদি আজ delivery না হয়, তাহলে system কি automatically attempt failed দেখাবে?

**১৭. এজেন্টঃ** স্যার, rider delivery complete না করলে status reattempt বা delivery rescheduled হতে পারে। আপনি app-এ নতুন date দেখতে পাবেন, আর incorrect remark থাকলে তা report করবেন।

**১৮. কাস্টমারঃ** কাল আবার পুরো দিন অপেক্ষা করতে পারবো না। Pickup point থেকে নেওয়ার option আছে?

**১৯. এজেন্টঃ** স্যার, আপনার shipment-এর জন্য pickup option এখনো enabled নয়। Courier confirmation ছাড়া hub বা pickup point-এ গেলে parcel দেওয়া নাও হতে পারে।

**২০. কাস্টমারঃ** আজকের delay-এর জন্য delivery charge refund চাওয়া যাবে?

**২১. এজেন্টঃ** স্যার, delivery delay record review করে charge adjustment বা compensation eligibility নির্ধারণ করা হয়। আমি আপনার request-এ এই inconvenience উল্লেখ করছি।

**২২. কাস্টমারঃ** Support reference নম্বর দিন। Rider update না দিলে আমি আবার call করবো।

**২৩. এজেন্টঃ** আপনার delivery follow-up reference DZ-OFD-২০২৬-০১১। আজ রাতের route update এবং পরবর্তী attempt schedule app notification-এ জানানো হবে।

**২৪. কাস্টমারঃ** ঠিক আছে সাবরিনা আপু। আমি gate security-কে জানিয়ে রাখছি, তবে call ছাড়া parcel নিতে দেবো না।

**২৫. এজেন্টঃ** সেটিই নিরাপদ সিদ্ধান্ত স্যার। Delivery agent-এর call না এলে parcel গ্রহণ করবেন না এবং order ID মিলিয়ে তারপর confirmation দেবেন।

---

## সিনারিও ১২ঃ গ্রামের ঠিকানায় courier delivery দিতে অস্বীকার করছে

> একজন rural customer পরিবারের জন্য water filter অর্ডার করেছেন। Courier delivery area coverage থাকা সত্ত্বেও rider ফোন করে নিকটস্থ বাজার থেকে parcel নিতে বলেছেন এবং বাড়িতে যেতে অস্বীকার করেছেন।

**১. কাস্টমারঃ** Daraz থেকে water filter অর্ডার করেছিলাম, কিন্তু courier বলছে আমার গ্রামের বাড়িতে যাবে না। আমাকে বাজারে গিয়ে parcel নিতে বলছে।

**২. এজেন্টঃ** Daraz customer care থেকে রাকিব বলছি। আপনার delivery experience-এর জন্য দুঃখিত স্যার। Order ID এবং district-এর নাম বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-৭১৩৫৯০২৪৬। আমার ঠিকানা বগুড়ার শিবগঞ্জ উপজেলার একটি গ্রামে।

**৪. এজেন্টঃ** ধন্যবাদ স্যার। Registered mobile number এবং app-এ যে full delivery address saved আছে, সেটি নিশ্চিত করবেন?

**৫. কাস্টমারঃ** নম্বর ০১৩৭৬৫৪৩২১০। ঠিকানায় গ্রাম, ইউনিয়ন, উপজেলা, district এবং কাছের বাজারের নাম সব লেখা আছে।

**৬. এজেন্টঃ** তথ্য যাচাই হয়েছে স্যার। আমি order coverage এবং courier route চেক করছি। Rider-এর call-এ কি exact reason বলা হয়েছে?

**৭. কাস্টমারঃ** সে বলেছে কাঁচা রাস্তা, তাই বাড়ির সামনে যাবে না। কিন্তু অন্য courier তো আমার বাড়ি পর্যন্ত parcel দেয়।

**৮. এজেন্টঃ** বুঝতে পারছি স্যার। Delivery safety issue থাকলে rider কাছের accessible point প্রস্তাব করতে পারে, তবে customer-এর সঙ্গে আলোচনা না করে delivery refusal করা উচিত নয়।

**৯. কাস্টমারঃ** আমি বাজারে যেতে পারি, কিন্তু সেটা আমার বাড়ি থেকে প্রায় ছয় কিলোমিটার দূরে। Product বড়, একা নিয়ে আসা কঠিন হবে।

**১০. এজেন্টঃ** স্যার, আমি courier supervisor-এর কাছে route review request করছি। তারা রাস্তার condition দেখে সম্ভব হলে doorstep delivery reattempt করবে।

**১১. কাস্টমারঃ** আমার বাবা অসুস্থ, water filter-এর জন্যই অর্ডার করেছি। আর কতদিন অপেক্ষা করতে হবে?

**১২. এজেন্টঃ** আপনার পরিবারের প্রয়োজনটি ticket-এ জরুরি হিসেবে লিখছি। তবে road accessibility যাচাই না করে আমি আজকের delivery নিশ্চিত বলে ভুল আশা দিতে চাই না।

**১৩. কাস্টমারঃ** যদি doorstep delivery সম্ভব না হয়, তাহলে কি order cancel করে টাকা ফেরত পাবো?

**১৪. এজেন্টঃ** জ্বী স্যার, courier service দিতে অক্ষম হলে customer-fault ছাড়া cancellation এবং refund review করা যায়। আপনার payment status অনুযায়ী process জানানো হবে।

**১৫. কাস্টমারঃ** আমি COD select করেছি। Cancel হলে কি কোনো penalty বা future account restriction হবে?

**১৬. এজেন্টঃ** না স্যার, courier coverage issue documented থাকলে আপনার account-এ cancellation penalty দেওয়ার কথা নয়। Investigation record-এ কারণটি পরিষ্কার রাখা হবে।

**১৭. কাস্টমারঃ** Seller-কে কি rural delivery সম্পর্কে আগে জানানো হবে? আবার অর্ডার করলে একই সমস্যা হতে পারে।

**১৮. এজেন্টঃ** স্যার, আপনার address coverage এবং delivery constraint seller ও courier team-এর কাছে note করছি। Reorder করার আগে product page-এ delivery availability check করবেন।

**১৯. কাস্টমারঃ** আমি কি অন্য courier বা Daraz Express বেছে নিতে পারবো? App-এ কোনো option দেখিনি।

**২০. এজেন্টঃ** স্যার, courier selection সব product বা location-এর জন্য customer-controlled নয়। Available service seller, warehouse এবং coverage অনুযায়ী system নির্ধারণ করে।

**২১. কাস্টমারঃ** Supervisor কতক্ষণে জানাবে তারা বাড়ি পর্যন্ত আসবে কিনা?

**২২. এজেন্টঃ** আপনার rural delivery review reference DZ-RUR-২০২৬-০১২। সাধারণত ২৪ ঘণ্টার মধ্যে route decision এবং next step SMS বা app-এ জানানো হয়।

**২৩. কাস্টমারঃ** ঠিক আছে রাকিব ভাই। Supervisor-এর call এলে আমি রাস্তার condition এবং landmark বুঝিয়ে দেবো।

**২৪. এজেন্টঃ** ধন্যবাদ স্যার। আপনার phone সচল রাখবেন এবং কোনো courier representative অতিরিক্ত charge চাইলে payment করার আগে আমাদের জানাবেন।

---

## সিনারিও ১৩ঃ রাতের delivery-তে rider customer-কে রাস্তার পাশে আসতে বলছে

> একজন মহিলা customer-এর parcel রাতের দিকে delivery-তে আসে। Rider apartment building-এ না এসে অন্ধকার রাস্তার পাশে customer-কে parcel নিতে বলেন, ফলে customer safety concern নিয়ে call করেন।

**১. কাস্টমারঃ** আপু, rider বলছে building-এ আসবে না, আমাকে main road-এর পাশে গিয়ে parcel নিতে হবে। এখন রাত, আমি একা বাইরে যেতে নিরাপদ বোধ করছি না।

**২. এজেন্টঃ** Daraz customer care থেকে নুসরাত বলছি ম্যাম। আপনার safety concern সম্পূর্ণ যুক্তিসংগত। Order ID এবং current delivery status বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-৮৪৫৬৭৮৯০১। Tracking-এ out for delivery দেখাচ্ছে, আর rider বলছে পাঁচ মিনিটের মধ্যে রাস্তার পাশে আসতে হবে।

**৪. এজেন্টঃ** ধন্যবাদ ম্যাম। আপনার registered number এবং building-এর প্রবেশপথে rider-এর ঢুকতে কোনো নির্দিষ্ট restriction আছে কিনা জানাবেন?

**৫. কাস্টমারঃ** নম্বর ০১৬৮৭৬৫৪৩২১। Security gate খোলা আছে, visitor entry হয়। Rider শুধু বলছে সে ভিতরে ঢুকবে না।

**৬. এজেন্টঃ** বুঝতে পারছি ম্যাম। আমি rider-এর delivery instruction এবং supervisor contact যাচাই করছি। আপনি একা বাইরে যাবেন না, আমি বিষয়টি এখনই operations team-এ পাঠাচ্ছি।

**৭. কাস্টমারঃ** ধন্যবাদ আপু। Parcel-এ আমার ছোট ভাইয়ের জরুরি school uniform আছে, কিন্তু safety ঝুঁকি নিয়ে নিতে চাই না।

**৮. এজেন্টঃ** আপনার প্রয়োজনটি বুঝতে পারছি ম্যাম। Rider-কে building gate পর্যন্ত আসতে বলা হবে, অথবা আপনার অনুমতিতে security guard-এর কাছে sealed parcel handover করা যেতে পারে।

**৯. কাস্টমারঃ** Security guard-এর কাছে দিতে পারেন, তবে আগে আমাকে call করতে হবে এবং parcel-এর label আমার order-এর সঙ্গে মিলতে হবে।

**১০. এজেন্টঃ** জ্বী ম্যাম, delivery instruction-এ আপনার অনুমোদিত receiver হিসেবে security desk উল্লেখ করছি। Parcel handover-এর আগে rider-কে registered number-এ call করতেই হবে।

**১১. কাস্টমারঃ** Rider যদি আবার অস্বীকার করে এবং order cancel করে দেয়, তাহলে কি আমার account-এ কোনো penalty হবে?

**১২. এজেন্টঃ** না ম্যাম, customer safety এবং doorstep access issue documented থাকলে cancellation customer fault হিসেবে ধরা উচিত নয়। আমি ticket-এ আপনার safety concern পরিষ্কারভাবে লিখছি।

**১৩. কাস্টমারঃ** Rider কি এখন building-এর সামনে আসছে? আমি security guard-কে জানিয়ে রাখবো।

**১৪. এজেন্টঃ** ম্যাম, supervisor rider-এর সঙ্গে যোগাযোগ করছেন। আমি আপনার call line-এ status note করছি, তবে rider-এর exact arrival time confirmation না পাওয়া পর্যন্ত নিশ্চিত করে বলছি না।

**১৫. কাস্টমারঃ** যদি আজ delivery না হয়, কাল কি নতুন rider দিয়ে reattempt করা যাবে?

**১৬. এজেন্টঃ** জ্বী ম্যাম, আজকের attempt unsuccessful হলে reattempt request করা যাবে। পরবর্তী rider-এর জন্য building gate, call-before-delivery এবং authorized receiver instruction যুক্ত থাকবে।

**১৭. কাস্টমারঃ** আমি কি rider-এর বিরুদ্ধে complaint করতে পারি? তার কথাবার্তা খুব চাপ দেওয়ার মতো ছিল।

**১৮. এজেন্টঃ** অবশ্যই ম্যাম। Safety instruction অমান্য এবং inappropriate delivery request দুটিই complaint record-এ যুক্ত করছি। Operations team call log ও route record review করবে।

**১৯. কাস্টমারঃ** Complaint reference এবং parcel না এলে refund-এর বিষয়টি জানাবেন?

**২০. এজেন্টঃ** আপনার reference DZ-SAF-২০২৬-০১৩। Delivery fail হলে cancellation বা refund eligibility review হবে; একই issue-তে নতুন order করার দরকার নেই।

**২১. কাস্টমারঃ** ঠিক আছে নুসরাত আপু। আমি বাইরে যাচ্ছি না, security desk-এই parcel নেবো।

**২২. এজেন্টঃ** সেটিই নিরাপদ সিদ্ধান্ত ম্যাম। Rider-এর call এবং parcel label যাচাই করে তারপর গ্রহণ করবেন। আপনার safety আমাদের কাছে অগ্রাধিকার।

---

## সিনারিও ১৪ঃ Delivery rider customer-এর সঙ্গে দুর্ব্যবহার করেছে

> একজন মহিলা customer delivery সময় product পরীক্ষা করতে চাইলে rider রূঢ় আচরণ করেন এবং দ্রুত parcel নিতে চাপ দেন। Customer rider conduct নিয়ে complaint করতে call করেন।

**১. কাস্টমারঃ** আমি খুব খারাপ আচরণের শিকার হয়েছি। Parcel নেওয়ার আগে product condition দেখতে চেয়েছিলাম, কিন্তু rider আমাকে অপমান করে চলে গেছে।

**২. এজেন্টঃ** Daraz customer care থেকে তানিম বলছি ম্যাম। আপনার সঙ্গে এমন আচরণের জন্য দুঃখিত। Order ID এবং incident-এর সময়টি বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-৩৬৭৮৯০১২৪। আজ বিকেল সাড়ে পাঁচটার দিকে rider এসেছিল, আমি শুধু box-এর seal ঠিক আছে কিনা দেখতে চেয়েছিলাম।

**৪. এজেন্টঃ** ধন্যবাদ ম্যাম। আপনার registered mobile number এবং rider কী ধরনের কথা বলেছেন, যতটা সম্ভব সংক্ষেপে জানাবেন?

**৫. কাস্টমারঃ** নম্বর ০১৮৯০১২৩৪৫৬। তিনি বললেন, “এত checking করলে parcel রেখে যাচ্ছি,” তারপর আমার সঙ্গে রূঢ়ভাবে কথা বলে চলে গেলেন।

**৬. এজেন্টঃ** ম্যাম, আপনার বক্তব্যটি আমি গুরুত্বসহকারে record করছি। Delivery record থেকে rider identity, route এবং attempted status যাচাই করতে একটু সময় দিন।

**৭. কাস্টমারঃ** আমি product নিইনি, কিন্তু tracking-এ delivered দেখাচ্ছে। Rider কি ইচ্ছা করে delivered mark করেছে?

**৮. এজেন্টঃ** ম্যাম, system-এ delivery completed দেখাচ্ছে, তবে আপনার confirmation বা signature record এখনো verify করা হয়নি। আমি এটিকে disputed delivery হিসেবে flag করছি।

**৯. কাস্টমারঃ** আমার কাছে rider-এর call history আছে। Building-এর CCTV-তেও তার আসার প্রমাণ থাকতে পারে।

**১০. এজেন্টঃ** এই তথ্যগুলো helpful হবে ম্যাম। Call time, CCTV availability এবং কোনো witness থাকলে complaint notes-এ যুক্ত করছি। আপনি চাইলে screenshot পরে Help Center-এ upload করতে পারবেন।

**১১. কাস্টমারঃ** আমি কি আবার একই rider-এর কাছ থেকে parcel নিতে বাধ্য? তার সঙ্গে আর interact করতে চাই না।

**১২. এজেন্টঃ** না ম্যাম, আপনার concern operations team-কে জানাচ্ছি। Reattempt হলে অন্য delivery representative assign করার request করা হবে, যদিও final assignment route availability-এর উপর নির্ভর করে।

**১৩. কাস্টমারঃ** Productটি prepaid, তাই refund নিয়ে চিন্তা হচ্ছে। Delivery না পেলে আমার টাকা কীভাবে সুরক্ষিত থাকবে?

**১৪. এজেন্টঃ** ম্যাম, disputed delivery investigation শেষ না হওয়া পর্যন্ত refund বা replacement claim বন্ধ হচ্ছে না। Parcel delivered প্রমাণিত না হলে payment recovery process review করা হবে।

**১৫. কাস্টমারঃ** Rider কি আমার address বা phone information অন্য কারো সঙ্গে share করতে পারে? আমি privacy নিয়েও চিন্তিত।

**১৬. এজেন্টঃ** আপনার personal information কেবল delivery purpose-এ ব্যবহারের কথা। Privacy concern-টিও complaint record-এ যুক্ত করছি এবং unauthorized sharing-এর কোনো evidence থাকলে upload করবেন।

**১৭. কাস্টমারঃ** আমি চাই Daraz management rider-এর বিরুদ্ধে formal action নিক। শুধু apology দিলে বিষয়টি শেষ হওয়া উচিত নয়।

**১৮. এজেন্টঃ** বুঝতে পারছি ম্যাম। এটি customer conduct এবং disputed delivery দুই category-তেই escalate করছি। Review result অনুযায়ী policy অনুযায়ী ব্যবস্থা নেওয়া হবে।

**১৯. কাস্টমারঃ** Complaint reference এবং investigation update কখন পাবো?

**২০. এজেন্টঃ** আপনার reference DZ-CON-২০২৬-০১৪। সাধারণত ৪৮ ঘণ্টার মধ্যে initial update দেওয়া হয়, আর disputed delivery resolution-এর পর final notification আসবে।

**২১. কাস্টমারঃ** ঠিক আছে তানিম ভাই। আমি CCTV এবং call record সংরক্ষণ করে রাখছি।

**২২. এজেন্টঃ** ধন্যবাদ ম্যাম। Evidence delete করবেন না এবং কোনো unknown person-কে payment বা personal information দেবেন না। আমরা আপনার ticket follow করছি।

---

## সিনারিও ১৫ঃ International seller-এর parcel customs-এ আটকে গেছে

> একজন customer international seller থেকে camera accessory অর্ডার করেছেন। Tracking-এ parcel customs clearance-এ আটকে আছে এবং customer জানতে চান additional documents বা customs payment দরকার হবে কিনা।

**১. কাস্টমারঃ** আমার international order অনেকদিন ধরে customs clearance-এ আটকে আছে। Tracking update নেই, আর parcelটি দেশে আসার পরও delivery date বদলাচ্ছে।

**২. এজেন্টঃ** Daraz customer care থেকে আরিফ বলছি স্যার। International shipment delay নিয়ে দুঃখিত। Order ID এবং product-এর নামটি বলবেন?

**৩. কাস্টমারঃ** Order ID DZ-৫৭৮৯০১২৩৬। Product camera tripod adapter, seller international। Expected delivery ছিল গত সপ্তাহে।

**৪. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered number এবং tracking-এ customs status কখন থেকে দেখা যাচ্ছে, সেটি জানাবেন?

**৫. কাস্টমারঃ** নম্বর ০১৭৬৫৪৩২১০৯। চার দিন ধরে “Held for customs inspection” দেখাচ্ছে, কোনো নতুন message আসেনি।

**৬. এজেন্টঃ** তথ্যগুলো যাচাই করছি স্যার। International shipment-এ customs authority parcel inspection, documentation বা applicable duty review করতে পারে। আমি seller এবং logistics partner-এর latest note দেখছি।

**৭. কাস্টমারঃ** আমার কি কোনো document upload করতে হবে? Product value কম, তবুও customs-এ এতদিন কেন আটকে আছে বুঝছি না।

**৮. এজেন্টঃ** স্যার, সাধারণত seller বা logistics partner customer-কে document দরকার হলে official notification দেয়। আপাতত আপনার account-এ কোনো document request দেখা যাচ্ছে না।

**৯. কাস্টমারঃ** Customs duty লাগলে কি delivery rider-এর হাতে cash দিতে হবে, নাকি app-এ payment option আসবে?

**১০. এজেন্টঃ** স্যার, কোনো duty বা official fee থাকলে authorized logistics channel থেকেই instruction আসবে। Unverified phone call বা personal number-এ টাকা পাঠাবেন না।

**১১. কাস্টমারঃ** Seller-এর সঙ্গে chat করেছি, কিন্তু তারা শুধু বলছে wait করতে। Daraz কি exact clearance date জানাতে পারে?

**১২. এজেন্টঃ** দুঃখিত স্যার, customs authority-এর internal timeline Daraz বা seller নির্ধারণ করতে পারে না। তবে shipment escalation পাঠিয়ে current document status এবং estimated next update চাওয়া যায়।

**১৩. কাস্টমারঃ** আমি এই accessory নিয়ে project presentation করতে চেয়েছিলাম। Delay হলে order cancel করে local seller থেকে কিনতে হবে।

**১৪. এজেন্টঃ** আপনার deadline note করছি স্যার। Customs release সম্ভব না হলে বা shipment lost হলে cancellation এবং refund eligibility আলাদাভাবে review করা হবে।

**১৫. কাস্টমারঃ** Cancel করলে কি customs-এর কারণে আমার account-এ কোনো penalty হবে?

**১৬. এজেন্টঃ** না স্যার, documented customs delay বা delivery failure customer misconduct নয়। তবে shipment already released হলে cancellation option সীমিত হতে পারে।

**১৭. কাস্টমারঃ** Parcel customs থেকে release হওয়ার পর delivery কতদিনে হতে পারে?

**১৮. এজেন্টঃ** স্যার, release scan পাওয়ার পর local courier handover হয়। এরপর destination এবং courier route অনুযায়ী সাধারণত কয়েক কর্মদিবস লাগতে পারে।

**১৯. কাস্টমারঃ** Tracking update না এলে কি আমি নিজে customs office-এ যোগাযোগ করবো?

**২০. এজেন্টঃ** স্যার, order reference ছাড়া সরাসরি যাওয়ার দরকার নেই। আগে logistics investigation result নিন; official contact information ছাড়া কোনো third party-র সঙ্গে কথা বলবেন না।

**২১. কাস্টমারঃ** আমার জন্য escalation ticket খুলুন এবং document দরকার হলে আমাকে জানাবেন।

**২২. এজেন্টঃ** আপনার international shipment reference DZ-CUS-২০২৬-০১৫। Logistics team customs status review করবে এবং update পাওয়া গেলে SMS বা app notification পাঠাবে।

**২৩. কাস্টমারঃ** ঠিক আছে আরিফ ভাই। Unknown caller-কে টাকা না দেওয়ার সতর্কতাটি কাজে লাগবে।

**২৪. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। Official Daraz channel ছাড়া duty, clearance fee বা refund সংক্রান্ত কোনো payment করবেন না।

---

## সিনারিও ১৬ঃ Delivery rider ভুল নম্বরে call করেছে

> একজন customer-এর order-এ phone number-এর একটি digit ভুল থাকায় rider অন্য নম্বরে যোগাযোগ করেছেন। Customer address ঠিক থাকলেও delivery missed হয়েছে এবং reattempt-এর জন্য call করেন।

**১. কাস্টমারঃ** আমার address ঠিক আছে, কিন্তু rider বলছে phone number ভুল। সে অন্য একজনকে call করেছে, তাই parcel delivery হয়নি।

**২. এজেন্টঃ** Daraz customer care থেকে সাবরিনা বলছি। Contact information mismatch-এর জন্য দুঃখিত স্যার। Order ID এবং tracking status জানাবেন?

**৩. কাস্টমারঃ** Order ID DZ-৬৯০১২৩৪৫৭। Tracking-এ delivery attempted দেখাচ্ছে, কিন্তু আমার phone-এ কোনো call আসেনি।

**৪. এজেন্টঃ** ধন্যবাদ স্যার। আপনার registered number এবং order details-এ যে contact number দেখা যাচ্ছে, দুটির মধ্যে পার্থক্যটি বলবেন?

**৫. কাস্টমারঃ** আমার সঠিক নম্বর ০১৯৮৭৬৫৪৩২১। Order-এ সম্ভবত ০১৯৮৭৬৫৪৩১২ লেখা হয়েছে, শেষ দুই digit উল্টো।

**৬. এজেন্টঃ** বুঝতে পেরেছি স্যার। আমি account profile এবং order snapshot আলাদা করে check করছি, কারণ order place করার পর contact change সব shipment-এ automatically apply নাও হতে পারে।

**৭. কাস্টমারঃ** Address একদম ঠিক আছে। শুধু number ভুল হওয়ায় কি parcel আবার seller-এর কাছে ফিরে যাবে?

**৮. এজেন্টঃ** স্যার, প্রথম attempt-এর পর এখনো return initiated হয়নি। আমি courier-কে correct contact number দিয়ে reattempt request পাঠাচ্ছি।

**৯. কাস্টমারঃ** আজকের মধ্যে delivery সম্ভব? আমি কাল সকালে শহরের বাইরে যাবো।

**১০. এজেন্টঃ** আপনার travel plan note করছি স্যার। Same-day reattempt courier route-এর উপর নির্ভর করবে, তাই আমি urgent request দিতে পারি কিন্তু নিশ্চিত সময় বলতে পারছি না।

**১১. কাস্টমারঃ** আমি আমার বাবাকে authorized receiver করতে চাই। Rider যদি আমাকে না পায়, তিনি parcel নিতে পারবেন?

**১২. এজেন্টঃ** জ্বী স্যার, account instruction-এ আপনার বাবার নাম এবং alternate contact যুক্ত করা যায়। Receiver-এর কাছে order ID এবং আপনার অনুমতি থাকা দরকার হবে।

**১৩. কাস্টমারঃ** বাবার নাম আব্দুল করিম, আর alternate number ০১৭১২৩৪৫৬৭৮। এগুলো কি rider দেখতে পাবে?

**১৪. এজেন্টঃ** Delivery instruction-এ authorized receiver ও alternate contact যুক্ত করছি স্যার। Privacy-এর জন্য কেবল প্রয়োজনীয় contact information courier view করবে।

**১৫. কাস্টমারঃ** ভুল নম্বরটি কি পুরোপুরি delete হবে? আমি চাই না ভবিষ্যৎ order-এ আবার একই সমস্যা হোক।

**১৬. এজেন্টঃ** স্যার, MyDaraz app-এর Account এবং Address Book section-এ গিয়ে saved address edit করুন। Correct phone number দিয়ে addressটি default হিসেবে set করলে পরের order-এ ভুল কমবে।

**১৭. কাস্টমারঃ** App-এ profile number ঠিক আছে, কিন্তু এই পুরনো address record-এ ভুল ছিল। আমি এখন update করছি।

**১৮. এজেন্টঃ** ভালো করছেন স্যার। Address update করার পর current order-এ change apply হয়েছে কিনা আমি system-এ check করছি, কারণ dispatched order আলাদাভাবে update করতে হয়।

**১৯. কাস্টমারঃ** যদি rider আবার ভুল নম্বরে call করে, তাহলে আমি কীভাবে বুঝবো সে আমার parcel-এর জন্য এসেছে?

**২০. এজেন্টঃ** স্যার, rider-এর কাছ থেকে order ID এবং product name confirm করবেন। কোনো OTP বা payment information অচেনা নম্বরে শেয়ার করবেন না।

**২১. কাস্টমারঃ** Reattempt request-এর reference number দিন। আমি বাবাকে আগে থেকে জানিয়ে রাখবো।

**২২. এজেন্টঃ** আপনার contact correction reference DZ-CON-২০২৬-০১৬। Courier team updated number-এ call করবে এবং alternate receiver instruction অনুযায়ী delivery চেষ্টা করবে।

**২৩. কাস্টমারঃ** ঠিক আছে সাবরিনা আপু। Address Book-এ number update করে বাবাকে authorized receiver হিসেবে জানিয়ে দিচ্ছি।

**২৪. এজেন্টঃ** ধন্যবাদ স্যার। Delivery confirmation-এর আগে parcel label এবং product details মিলিয়ে নেবেন। আপনার travel-এর আগেই update দেওয়ার চেষ্টা করা হবে।

---

## সিনারিও ১৭ঃ প্রোডাক্টের রং ছবির সঙ্গে মিলছে না

> একজন customer website-এর ছবিতে navy blue shirt দেখে order করেছিলেন। Delivery-এর পর তিনি দেখেন shirt-এর রং অনেক হালকা এবং listing image-এর সঙ্গে যথেষ্ট পার্থক্য রয়েছে।

**১. কাস্টমারঃ** আমি navy blue shirt অর্ডার করেছিলাম, কিন্তু যে shirt এসেছে সেটি অনেক হালকা blue। ছবির সঙ্গে রং একদম মিলছে না।

**২. এজেন্টঃ** Daraz customer care থেকে ফারিয়া বলছি ম্যাম। Product color mismatch নিয়ে আপনার অসুবিধাটি বুঝতে পারছি। আপনি কি item-এর label এবং received color নিশ্চিত করবেন?

**৩. কাস্টমারঃ** Label-এ navy blue লেখা আছে, কিন্তু বাস্তবে এটি faded sky blue-এর মতো দেখাচ্ছে। ছবিতে shirt অনেক গাঢ় এবং premium মনে হয়েছিল।

**৪. এজেন্টঃ** ম্যাম, আপনার product page-এর color option এবং received item-এর ছবি মিলিয়ে দেখা দরকার। অনুগ্রহ করে product-এর ছবি, label এবং packaging-এর ছবি সংরক্ষণ করবেন।

**৫. কাস্টমারঃ** আমি ইতিমধ্যে daylight-এ ছবি তুলেছি। ছবিতে পরিষ্কার দেখা যাচ্ছে, listing-এর navy blue আর এই shirt-এর color একই নয়।

**৬. এজেন্টঃ** বুঝতে পারছি ম্যাম। কিছু screen বা lighting-এর কারণে সামান্য color variation হতে পারে, তবে noticeable mismatch হলে এটি return review-এর আওতায় পড়তে পারে।

**৭. কাস্টমারঃ** এখানে সামান্য variation নয়, পুরো shade আলাদা। আমি অফিসে পরার জন্য কিনেছিলাম, এই রং আমার পছন্দ হচ্ছে না।

**৮. এজেন্টঃ** আপনার ব্যবহারিক সমস্যাটি বুঝলাম ম্যাম। আমি return reason হিসেবে “Product color does not match listing” নির্বাচন করে request process বুঝিয়ে দিচ্ছি।

**৯. কাস্টমারঃ** আমি replacement চাই না। একই seller-এর কাছ থেকে আবার order করলে আবার ভুল color আসার ভয় আছে।

**১০. এজেন্টঃ** তাহলে ম্যাম, refund preference request-এ উল্লেখ করছি। Seller review এবং product condition যাচাইয়ের পর refund approval দেওয়া হবে।

**১১. কাস্টমারঃ** Shirt আমি একবার try করেছি, কিন্তু বাইরে পরিনি এবং কোনো tag খুলিনি। এতে return করতে সমস্যা হবে?

**১২. এজেন্টঃ** Tag, packaging এবং product condition অক্ষত থাকলে return review সহজ হয় ম্যাম। Shirt ধোয়া, ব্যবহার বা perfume লাগানো থেকে বিরত থাকবেন।

**১৩. কাস্টমারঃ** Return pickup কি বাসা থেকে হবে? আমার অফিসের সময় courier এলে বাসায় কাউকে থাকতে হবে।

**১৪. এজেন্টঃ** Pickup schedule হওয়ার আগে SMS বা app notification আসবে ম্যাম। আপনি চাইলে available pickup date অনুযায়ী slot নির্বাচন করতে পারবেন।

**১৫. কাস্টমারঃ** Seller যদি বলে color variation স্বাভাবিক, তাহলে কি আমার return বাতিল হয়ে যাবে?

**১৬. এজেন্টঃ** ম্যাম, seller-এর বক্তব্যের পাশাপাশি listing image, selected variant এবং আপনার evidence review করা হবে। Final decision কেবল seller-এর কথার উপর নির্ভর করবে না।

**১৭. কাস্টমারঃ** Product page-এর screenshot কি এখনই upload করবো? পরে listing image বদলে গেলে সমস্যা হতে পারে।

**১৮. এজেন্টঃ** জ্বী ম্যাম, selected color option এবং original listing-এর screenshot এখনই upload করে রাখুন। এটি claim review-এর সময় গুরুত্বপূর্ণ evidence হবে।

**১৯. কাস্টমারঃ** Refund approved হলে আমি যে delivery fee দিয়েছি, সেটিও কি ফেরত পাবো?

**২০. এজেন্টঃ** ম্যাম, product mismatch প্রমাণিত হলে refund এবং applicable delivery charge policy অনুযায়ী review করা হবে। Approval result notification-এ বিস্তারিত amount দেখবেন।

**২১. কাস্টমারঃ** Return request numberটা বলবেন? আমি ছবি আর screenshot upload করে রাখছি।

**২২. এজেন্টঃ** আপনার return reference DZ-COL-২০২৬-০১৭। Request submit করার পর pickup confirmation এবং seller review status app-এ দেখতে পারবেন।

**২৩. কাস্টমারঃ** ঠিক আছে ফারিয়া আপু। Shirtটি tag-সহ আগের মতো রেখে ছবি upload করছি।

**২৪. এজেন্টঃ** ভালো করবেন ম্যাম। Pickup-এর সময় parcel handover receipt নেবেন এবং refund confirmation না আসা পর্যন্ত reference numberটি সংরক্ষণ করবেন।

---

## সিনারিও ১৮ঃ নতুন product হিসেবে order করে ব্যবহৃত item পাওয়া গেছে

> একজন customer Daraz-এ “Brand New” লেখা একটি smartwatch কিনেছেন। Delivery-এর পর তিনি দেখেন watch-এ scratches, previous user data এবং charging history-এর চিহ্ন রয়েছে।

**১. কাস্টমারঃ** আমি নতুন smartwatch কিনেছিলাম, কিন্তু box খুলে মনে হচ্ছে এটি আগে কেউ ব্যবহার করেছে। Screen-এ scratches আর পুরনো data দেখা যাচ্ছে।

**২. এজেন্টঃ** Daraz customer care থেকে আরিফ বলছি স্যার। নতুন product-এর বদলে used item পাওয়া গুরুতর বিষয়। আপনি কি device চালু করার আগে কোনো ছবি তুলেছেন?

**৩. কাস্টমারঃ** হ্যাঁ, unboxing video করেছি। Watch চালু করলে আগের একজনের fitness data আর কিছু notification দেখা যায়।

**৪. এজেন্টঃ** স্যার, খুব ভালো করেছেন। অনুগ্রহ করে device reset করবেন না, account-এ login করবেন না এবং unboxing video original অবস্থায় সংরক্ষণ করবেন।

**৫. কাস্টমারঃ** Box-এর seal বাইরে থেকে ঠিক ছিল, কিন্তু watch-এর strap-এ দাগ এবং screen-এ ছোট scratches আছে।

**৬. এজেন্টঃ** বুঝতে পারছি স্যার। এটি “Used or previously opened product sold as new” reason-এ report করা হচ্ছে। Seller এবং fulfillment record দুই দিক থেকেই investigation হবে।

**৭. কাস্টমারঃ** আমি full refund চাই। এমন device ব্যবহার করা security risk হতে পারে, বিশেষ করে আগের user-এর data যখন ছিল।

**৮. এজেন্টঃ** আপনার concern একদম যৌক্তিক স্যার। Return request-এ full refund preference যোগ করছি এবং productটি ব্যবহার না করার নির্দেশ দিচ্ছি।

**৯. কাস্টমারঃ** Charger আর extra strap box-এর ভিতর আছে। সবকিছু একসঙ্গে ফেরত দিতে হবে?

**১০. এজেন্টঃ** জ্বী স্যার, watch, charger, strap, manual এবং packaging-এর সব অংশ একসঙ্গে রাখবেন। কিছু missing থাকলে inspection delay হতে পারে।

**১১. কাস্টমারঃ** Seller কি আমাকে সরাসরি call করে settlement করতে পারে? আমি platform-এর বাইরে কোনো কথা বলতে চাই না।

**১২. এজেন্টঃ** স্যার, সব communication Daraz chat বা official support channel-এ রাখবেন। Seller ব্যক্তিগত নম্বরে refund বা settlement প্রস্তাব দিলে payment বা personal information দেবেন না।

**১৩. কাস্টমারঃ** আমি কি seller-এর বিরুদ্ধে counterfeit বা fraud complaint করতে পারি?

**১৪. এজেন্টঃ** স্যার, Used product হিসেবে report করা হচ্ছে। Investigation-এ intentional misrepresentation পাওয়া গেলে seller conduct review এবং marketplace action নেওয়া হতে পারে।

**১৫. কাস্টমারঃ** Return pickup-এর সময় courier agent কি unboxing video দেখতে চাইবে?

**১৬. এজেন্টঃ** প্রয়োজনে inspection team evidence চাইতে পারে স্যার, তবে pickup agent-এর কাছে phone unlock বা personal account information দেওয়ার দরকার নেই।

**১৭. কাস্টমারঃ** Device-এ আগের user-এর data ছিল, তাই privacy নিয়ে চিন্তা হচ্ছে। আমি কি watch-এর network বন্ধ করে রাখবো?

**১৮. এজেন্টঃ** জ্বী স্যার, device ব্যবহার না করে power off করে রাখুন। কোনো account access, pairing বা reset করবেন না; investigation-এর জন্য original condition গুরুত্বপূর্ণ।

**১৯. কাস্টমারঃ** Seller যদি product genuine বলে claim করে, তাহলে আমার video কি যথেষ্ট evidence হবে?

**২০. এজেন্টঃ** স্যার, unboxing video, scratches-এর ছবি, previous data এবং packaging label একসঙ্গে review করা হবে। Evidence clear থাকলে আপনার claim শক্তিশালী হবে।

**২১. কাস্টমারঃ** আমার refund request কতদিনে review হবে?

**২২. এজেন্টঃ** আপনার case reference DZ-AUT-২০২৬-০১৮। Pickup এবং inspection শেষ হলে refund decision app notification-এ জানানো হবে।

**২৩. কাস্টমারঃ** ঠিক আছে আরিফ ভাই। আমি device বন্ধ রেখে সব accessories এবং video সংরক্ষণ করছি।

**২৪. এজেন্টঃ** ধন্যবাদ স্যার। Productটি charge বা pair করবেন না, এবং pickup-এর সময় handover receipt সংগ্রহ করবেন। আপনার privacy concern-টিও case notes-এ যুক্ত করা হয়েছে।

---

## সিনারিও ১৯ঃ Size chart অনুসরণ করেও পোশাক tight হয়েছে

> একজন customer listing-এর size chart অনুযায়ী kurti order করেছেন। Delivery-এর পর তিনি দেখেন পোশাকটি measurement অনুযায়ী নয় এবং পরলে অস্বস্তিকরভাবে tight লাগে।

**১. কাস্টমারঃ** আপু, আমি size chart দেখে kurti order করেছিলাম, কিন্তু delivery-এর পর দেখি এটি অনেক tight। Listing-এর measurement-এর সঙ্গে মিলছে না।

**২. এজেন্টঃ** Daraz customer care থেকে নুসরাত বলছি ম্যাম। Size mismatch নিয়ে আপনার অসুবিধার জন্য দুঃখিত। আপনি কি garment-এর measurement নিয়েছেন?

**৩. কাস্টমারঃ** হ্যাঁ, বুকের মাপ listing-এ ৪২ inch লেখা ছিল, কিন্তু received kurti মেপে প্রায় ৩৯ inch পাচ্ছি।

**৪. এজেন্টঃ** ম্যাম, measurement নেওয়ার সময় garmentটি flat surface-এ রেখে দুই পাশ মেপে পুরো width হিসাব করেছেন তো?

**৫. কাস্টমারঃ** জ্বী, flat করে মেপেছি এবং দুই পাশের measurement যোগ করেছি। আমার কাছে measurement-এর ছবিও আছে।

**৬. এজেন্টঃ** খুব ভালো ম্যাম। Listing size chart এবং received product-এর measurement-এর ছবি একসঙ্গে upload করবেন, যাতে mismatch পরিষ্কারভাবে দেখা যায়।

**৭. কাস্টমারঃ** আমি exchange চাই। একই design-এর বড় size যদি থাকে, তাহলে refund না নিয়ে সেটিই নিতে চাই।

**৮. এজেন্টঃ** আপনার preference request-এ লিখে দিচ্ছি ম্যাম। Seller-এর inventory থাকলে size exchange option review করা হবে; না থাকলে refund alternative দেওয়া হবে।

**৯. কাস্টমারঃ** Kurti একবার পরে দেখেছি, কিন্তু বাইরে পরিনি। Tag এখনো attached আছে, তবে packaging খুলে ফেলেছি।

**১০. এজেন্টঃ** ম্যাম, try-on করা সাধারণত size check-এর অংশ হতে পারে, যদি product ব্যবহৃত বা damaged না হয়। Tag এবং original packaging যতটা সম্ভব অক্ষত রাখবেন।

**১১. কাস্টমারঃ** Seller বলছে sale item exchange করা যায় না। কিন্তু size chart যদি ভুল হয়, তাহলে কি policy আলাদা হবে?

**১২. এজেন্টঃ** ম্যাম, সাধারণ preference change আর listing measurement mismatch এক বিষয় নয়। আপনার evidence অনুযায়ী claimটি product information mismatch হিসেবে review হবে।

**১৩. কাস্টমারঃ** Return pickup-এর আগে কি tailor-এর কোনো measurement report দরকার হবে?

**১৪. এজেন্টঃ** সাধারণত দরকার হয় না ম্যাম। আপনার measurement photo, size chart screenshot এবং product tag যথেষ্ট প্রাথমিক evidence হিসেবে কাজ করবে।

**১৫. কাস্টমারঃ** আমি যদি exchange পাই, courier কি পুরনো kurti নিয়ে নতুন size একই সময়ে দেবে?

**১৬. এজেন্টঃ** ম্যাম, exchange process seller এবং fulfillment availability-এর উপর নির্ভর করে। সাধারণত আগে returned item inspection হয়, তারপর replacement shipment তৈরি করা হয়।

**১৭. কাস্টমারঃ** Eid-এর আগে outfitটি দরকার। Exchange দেরি হলে আমার জন্য আর ব্যবহারযোগ্য থাকবে না।

**১৮. এজেন্টঃ** আপনার deadline note করছি ম্যাম। তবে replacement delivery date inventory confirm না হওয়া পর্যন্ত নিশ্চিত বলা ঠিক হবে না; refund option দ্রুততর হতে পারে।

**১৯. কাস্টমারঃ** তাহলে exchange আর refund-এর মধ্যে আমি পরে সিদ্ধান্ত নিতে পারবো?

**২০. এজেন্টঃ** জ্বী ম্যাম, Seller response ও inspection result আসার পর available options দেখতে পারবেন। Request-এ exchange preference রাখা হয়েছে, কিন্তু final option notification-এ থাকবে।

**২১. কাস্টমারঃ** Request reference এবং ছবি upload করার শেষ সময়টা বলবেন?

**২২. এজেন্টঃ** আপনার size mismatch reference DZ-SIZ-২০২৬-০১৯। যত দ্রুত সম্ভব, preferably আজকের মধ্যেই ছবি upload করবেন, যাতে review শুরু হতে দেরি না হয়।

**২৩. কাস্টমারঃ** ঠিক আছে নুসরাত আপু। আমি measurement, size chart এবং tag-এর ছবি এখনই পাঠাচ্ছি।

**২৪. এজেন্টঃ** ধন্যবাদ ম্যাম। Kurti ধোবেন বা alter করবেন না; alteration হলে size mismatch verification জটিল হয়ে যেতে পারে।

---

## সিনারিও ২০ঃ Electronics product delivery-এর পর চালু হচ্ছে না

> একজন customer Daraz থেকে Bluetooth speaker কিনেছেন। Delivery-এর পর charging, power button এবং alternate cable পরীক্ষা করেও speaker চালু হয়নি।

**১. কাস্টমারঃ** আমার Bluetooth speaker আজ এসেছে, কিন্তু একদম চালু হচ্ছে না। Power button চাপলেও কোনো light বা sound পাচ্ছি না।

**২. এজেন্টঃ** Daraz customer care থেকে রাকিব বলছি স্যার। Delivery-এর পরপরই এমন সমস্যা হওয়ায় দুঃখিত। Productটি কি charge করার চেষ্টা করেছেন?

**৩. কাস্টমারঃ** জ্বী, প্রায় এক ঘণ্টা charge দিয়েছি। Original cable এবং অন্য একটি cable দুটো দিয়েই চেষ্টা করেছি, তবুও response নেই।

**৪. এজেন্টঃ** স্যার, charging port-এ কোনো visible damage, loose connection বা burnt smell আছে কি? নিরাপত্তার জন্য damaged হলে আর charge দেবেন না।

**৫. কাস্টমারঃ** Port ঠিক দেখাচ্ছে, burnt smell নেই। কিন্তু box-এর ভিতরের manual-এ product test করার কোনো নির্দেশনা পাইনি।

**৬. এজেন্টঃ** বুঝতে পারছি স্যার। Power button সাধারণত কয়েক সেকেন্ড ধরে রাখতে হয়, তবে repeated charging বা force reset না করাই ভালো। আমি return process শুরু করছি।

**৭. কাস্টমারঃ** আমি replacement চাই। Productটি gift হিসেবে কিনেছিলাম, refund নিয়ে আবার নতুন করে order করলে সময় লাগবে।

**৮. এজেন্টঃ** আপনার replacement preference request-এ যোগ করছি স্যার। Seller stock এবং technical inspection অনুযায়ী replacement approve হতে পারে।

**৯. কাস্টমারঃ** Speaker-এর box-এর seal আগে খোলা ছিল কিনা নিশ্চিত নই। বাইরে কোনো বড় damage ছিল না, তাই তখন check করিনি।

**১০. এজেন্টঃ** স্যার, unboxing photo বা video থাকলে upload করবেন। Box, serial label, accessories এবং device-এর power failure-এর ছবি সংরক্ষণ করুন।

**১১. কাস্টমারঃ** Unboxing video নেই, তবে power button চাপার ভিডিও করেছি। Device একদম response করছে না।

**১২. এজেন্টঃ** এই video যথেষ্ট প্রাথমিক evidence হিসেবে কাজে লাগবে স্যার। Productটি খুলে repair করার চেষ্টা করবেন না, এতে warranty বা return inspection প্রভাবিত হতে পারে।

**১৩. কাস্টমারঃ** Seller আমাকে বলেছে local service center-এ নিয়ে যেতে। Daraz থেকে কেনার পর সেটা কি আমার দায়িত্ব?

**১৪. এজেন্টঃ** স্যার, নতুন অবস্থায় কাজ না করা product-এর ক্ষেত্রে আগে Daraz return বা replacement case follow করবেন। Official ticket ছাড়া নিজে repair করাতে যাবেন না।

**১৫. কাস্টমারঃ** Pickup কি doorstep থেকে হবে? Speaker ছোট হলেও আমি ব্যস্ত থাকি, courier office-এ যাওয়া সম্ভব নয়।

**১৬. এজেন্টঃ** আপনার address coverage থাকলে doorstep pickup schedule করা হবে স্যার। Pickup date এবং time window SMS বা app notification-এ জানানো হবে।

**১৭. কাস্টমারঃ** যদি inspection-এ তারা বলে product কাজ করছিল, তাহলে কি replacement পাবো না?

**১৮. এজেন্টঃ** স্যার, inspection-এর সময় power test, serial number এবং physical condition দেখা হবে। আপনার video এবং charging attempts-এর তথ্য review team-কে দেওয়া হচ্ছে।

**১৯. কাস্টমারঃ** Replacement approve হলে নতুন speaker আসতে কতদিন লাগতে পারে?

**২০. এজেন্টঃ** Seller stock confirm হওয়ার পর replacement dispatch হবে। Exact timeline inspection complete এবং shipment create হওয়ার পর app-এ দেখানো হবে।

**২১. কাস্টমারঃ** আমি চাই না dead product রেখে seller replacement delay করুক। Case-টি priority হিসেবে mark করবেন?

**২২. এজেন্টঃ** জ্বী স্যার, এটি “Dead on arrival” হিসেবে priority review-তে পাঠাচ্ছি। আপনার reference DZ-DOA-২০২৬-০২০, এটিতে সব evidence যুক্ত থাকবে।

**২৩. কাস্টমারঃ** ঠিক আছে রাকিব ভাই। Speaker খুলে দেখবো না, packaging আর video সংরক্ষণ করছি।

**২৪. এজেন্টঃ** খুব ভালো করবেন স্যার। Device আর charge দেবেন না, accessoriesসহ original packaging-এ রাখবেন এবং pickup-এর সময় handover receipt নেবেন।

---

## সিনারিও ২১ঃ আসল বলে বিক্রি করা নকল প্রোডাক্ট পাওয়া গেছে

> একজন customer Daraz-এ branded perfume অর্ডার করেছেন। Delivery-এর পর packaging, fragrance এবং serial information দেখে তার নকল product মনে হয়েছে।

**১. কাস্টমারঃ** ভাইয়া, আমি branded perfume অর্ডার করেছিলাম, কিন্তু box আর fragrance দেখে মনে হচ্ছে এটি নকল। Product page-এ original লেখা ছিল।

**২. এজেন্টঃ** Daraz customer care থেকে আরিফ বলছি স্যার। Authenticity concern-টি গুরুত্বসহকারে দেখছি। Product-এর box, seal এবং seller information কী লক্ষ্য করেছেন?

**৩. কাস্টমারঃ** Box-এর printing ঝাপসা, batch code ঠিকমতো পড়া যায় না, আর fragrance পাঁচ মিনিটের মধ্যেই উধাও হয়ে গেছে।

**৪. এজেন্টঃ** স্যার, এমন লক্ষণ product verification-এর জন্য গুরুত্বপূর্ণ। Box, bottle, batch code, seal এবং listing-এর screenshot আলাদা করে capture করে রাখবেন।

**৫. কাস্টমারঃ** আমি seller-এর rating দেখে order করেছিলাম। অনেক customer five-star review দিয়েছে, তাই সন্দেহ করিনি।

**৬. এজেন্টঃ** বুঝতে পারছি স্যার। Rating একা authenticity নিশ্চিত করে না; Daraz তদন্তে listing claim, seller documents, inventory source এবং customer evidence একসঙ্গে review করে।

**৭. কাস্টমারঃ** Perfume আমি একবার spray করে দেখেছি, কিন্তু এত দ্রুত সমস্যা বুঝিনি। এতে কি return reject হতে পারে?

**৮. এজেন্টঃ** স্যার, authenticity যাচাইয়ের জন্য limited testing স্বাভাবিক হতে পারে। তবে আর ব্যবহার করবেন না এবং bottle বা packaging-এ কোনো পরিবর্তন করবেন না।

**৯. কাস্টমারঃ** আমি full refund চাই। এই product ব্যবহার করলে skin reaction হতে পারে, তাই health concern-ও আছে।

**১০. এজেন্টঃ** আপনার safety concern যুক্তিসংগত স্যার। আমি authenticity dispute এবং return request দুটোই record করছি, যাতে caseটি সাধারণ preference return হিসেবে না যায়।

**১১. কাস্টমারঃ** Seller আমাকে chat-এ বলেছে, “Original না হলে টাকা লাগবে না,” কিন্তু কোনো invoice বা source document দেয়নি।

**১২. এজেন্টঃ** Seller-এর chat screenshot সংরক্ষণ করবেন স্যার। Daraz-এর official chat-এর বাইরে WhatsApp বা ব্যক্তিগত নম্বরে কোনো settlement করবেন না।

**১৩. কাস্টমারঃ** Productটি কি laboratory বা brand authority পরীক্ষা করবে? আমি সত্যিই জানতে চাই এটি fake কিনা।

**১৪. এজেন্টঃ** স্যার, প্রয়োজনে product verification team packaging, batch information এবং seller documentation পরীক্ষা করবে। সব ক্ষেত্রে laboratory test হয় না, তবে evidence অনুযায়ী সিদ্ধান্ত নেওয়া হবে।

**১৫. কাস্টমারঃ** Seller যদি return নিতে না চায়, তাহলে কি Daraz directly intervene করবে?

**১৬. এজেন্টঃ** জ্বী স্যার, Dispute team claimটি review করবে। Seller response না দিলেও investigation বন্ধ হবে না, এবং policy অনুযায়ী পরবর্তী সিদ্ধান্ত নেওয়া হবে।

**১৭. কাস্টমারঃ** Pickup-এর সময় courier agent কি product খুলে check করবে?

**১৮. এজেন্টঃ** সাধারণত courier sealed parcel collect করবে স্যার। Detailed inspection পরে designated team করবে, তাই evidence এবং original condition বজায় রাখবেন।

**১৯. কাস্টমারঃ** Seller-এর account-এর বিরুদ্ধে ব্যবস্থা নেওয়া হবে? নকল product অন্য customer-দেরও যেতে পারে।

**২০. এজেন্টঃ** Investigation-এ violation প্রমাণিত হলে seller listing restriction, penalty বা account action-এর আওতায় আসতে পারে স্যার।

**২১. কাস্টমারঃ** আমার case number এবং photo upload করার নিয়মটা বলবেন?

**২২. এজেন্টঃ** আপনার authenticity dispute reference DZ-AUT-২০২৬-০২১। My Orders থেকে Return/Refund section খুলে bottle, box, batch code এবং chat screenshot upload করবেন।

**২৩. কাস্টমারঃ** ঠিক আছে আরিফ ভাই। আমি product আর ব্যবহার করবো না এবং সব evidence আজই পাঠিয়ে দেবো।

**২৪. এজেন্টঃ** ধন্যবাদ স্যার। Skin irritation হলে product সঙ্গে সঙ্গে বন্ধ করবেন এবং প্রয়োজনে চিকিৎসকের পরামর্শ নেবেন। আমরা case update official channel-এ জানাবো।

---

## সিনারিও ২২ঃ Expired food product delivery হয়েছে

> একজন housewife Daraz থেকে packaged snacks অর্ডার করেছেন। Delivery-এর পর তিনি দেখেন কয়েকটি item-এর expiry date পার হয়ে গেছে এবং একটি packet ফুলে আছে।

**১. কাস্টমারঃ** আপু, আজ grocery parcel পেয়েছি। কিছু packet-এর expiry date পার হয়ে গেছে, আর একটি packet অস্বাভাবিকভাবে ফুলে আছে।

**২. এজেন্টঃ** Daraz customer care থেকে নুসরাত বলছি ম্যাম। Expired বা swollen food item পাওয়া নিরাপত্তার বিষয়। দয়া করে কোনো item taste করবেন না।

**৩. কাস্টমারঃ** আমি কিছু খাইনি। দুইটি biscuit packet expired, আর juice packet-এর cap-এর কাছে leakage-এর দাগ আছে।

**৪. এজেন্টঃ** ম্যাম, productগুলো আলাদা করে রাখবেন এবং expiry date, batch number, seal ও outer parcel-এর পরিষ্কার ছবি তুলবেন।

**৫. কাস্টমারঃ** আমি ছবি তুলেছি। কিন্তু order-এ মোট আটটি item ছিল, সবগুলো কি return করতে হবে?

**৬. এজেন্টঃ** ম্যাম, যেগুলো expired, leaking বা damaged সেগুলো claim-এর জন্য আলাদা করুন। তবে order review-এর সময় পুরো grocery shipment-এর তথ্য দিন।

**৭. কাস্টমারঃ** আমি partial refund চাই না, কারণ একই seller-এর কাছ থেকে food quality নিয়ে আর trust করতে পারছি না।

**৮. এজেন্টঃ** আপনার concern বুঝলাম ম্যাম। আপনি affected items-এর refund চাইছেন, নাকি পুরো grocery order return করতে চান, request-এ preference স্পষ্ট করে দিতে পারেন।

**৯. কাস্টমারঃ** শুধু expired items-এর টাকা ফেরত চাই। Fresh itemsগুলো ঠিক আছে, সেগুলো ফেরত দিলে অপচয় হবে।

**১০. এজেন্টঃ** ঠিক আছে ম্যাম, আমি affected item-only refund request হিসেবে note করছি। Food safety evidence থাকায় seller review দ্রুত করা হবে।

**১১. কাস্টমারঃ** Expired packetগুলো কি courier-কে ফেরত দিতে হবে? এগুলো আবার transport করা নিরাপদ মনে হচ্ছে না।

**১২. এজেন্টঃ** ম্যাম, Pickup instruction-এ product condition উল্লেখ করছি। Courier যদি item collect করতে আসে, sealed outer bag-এ রাখবেন এবং leakage থাকলে আগে জানাবেন।

**১৩. কাস্টমারঃ** Packet ফুলে আছে, আমি এটিকে ছুঁতেও চাই না। Disposal করলে কি refund claim বাতিল হবে?

**১৪. এজেন্টঃ** ম্যাম, safety risk থাকলে product সংরক্ষণ না করে disposal করতে হতে পারে। Disposal-এর আগে expiry, seal এবং condition-এর timestampসহ ছবি রাখবেন এবং support note-এ জানাবেন।

**১৫. কাস্টমারঃ** Seller বলছে expiry date নাকি printing mistake। আমি কীভাবে নিশ্চিত হবো?

**১৬. এজেন্টঃ** Seller-এর explanation একা final নয় ম্যাম। Batch information, product photo, invoice এবং warehouse record review করে Daraz সিদ্ধান্ত নেবে।

**১৭. কাস্টমারঃ** এই seller-এর product listing-এ “fresh stock” লেখা ছিল। Misleading description-এর বিরুদ্ধে report করতে চাই।

**১৮. এজেন্টঃ** অবশ্যই ম্যাম। Product quality complaint-এর পাশাপাশি misleading listing report করছি। Listing screenshot থাকলে evidence হিসেবে upload করবেন।

**১৯. কাস্টমারঃ** আমার ছোট বাচ্চা packet খুলতে যাচ্ছিল। এই ধরনের ভুল যেন অন্য কারো সঙ্গে না হয়।

**২০. এজেন্টঃ** আপনার সতর্কতা খুব গুরুত্বপূর্ণ ম্যাম। আমরা seller quality team-কে বিষয়টি পাঠাচ্ছি, আর আপনি food item খাওয়ানোর আগে expiry ও seal অবশ্যই যাচাই করবেন।

**২১. কাস্টমারঃ** Refund request-এর reference এবং evidence upload-এর deadline জানাবেন?

**২২. এজেন্টঃ** আপনার food safety reference DZ-FOD-২০২৬-০২২। আজকের মধ্যে expiry, leakage, batch এবং invoice-এর ছবি upload করলে review দ্রুত শুরু হবে।

**২৩. কাস্টমারঃ** ঠিক আছে নুসরাত আপু। Expired item আলাদা রাখছি এবং কোনোটা ব্যবহার করছি না।

**২৪. এজেন্টঃ** খুব ভালো করবেন ম্যাম। Swollen বা leaking packet খুলবেন না, শিশুদের কাছ থেকে দূরে রাখবেন এবং official update না আসা পর্যন্ত seller-এর ব্যক্তিগত নম্বরে যোগাযোগ করবেন না।

---

## সিনারিও ২৩ঃ Furniture-এর assembly parts missing

> একজন small business owner Daraz থেকে office shelf অর্ডার করেছেন। Delivery-এর পর কাঠের panels থাকলেও screws, brackets এবং assembly manual পাওয়া যায়নি।

**১. কাস্টমারঃ** আমার office shelf এসেছে, কিন্তু assembly করার screws আর brackets নেই। শুধু wooden panels দিয়ে কীভাবে furniture বানাবো?

**২. এজেন্টঃ** Daraz customer care থেকে তানিম বলছি স্যার। Missing parts-এর কারণে আপনার সমস্যা হয়েছে, দুঃখিত। Box-এর ভিতরের সবকিছু পরীক্ষা করেছেন?

**৩. কাস্টমারঃ** জ্বী, panels, দুইটি side board আর shelf আছে। Hardware packet এবং assembly manual কোনোটাই নেই।

**৪. এজেন্টঃ** স্যার, packaging-এর ভিতরে কোনো ছোট compartment বা cardboard flap আছে কিনা আরেকবার দেখবেন? Furniture hardware কখনো কখনো আলাদা pouch-এ থাকে।

**৫. কাস্টমারঃ** পুরো box খুলে দেখেছি। Delivery-এর সময় carton-এর একপাশ ছেঁড়া ছিল, সম্ভবত hardware packet সেখান থেকে বেরিয়ে গেছে।

**৬. এজেন্টঃ** বুঝতে পারছি স্যার। Outer carton damage, missing compartment এবং received panels-এর ছবি সংরক্ষণ করবেন। এগুলো transit loss নাকি seller packing issue বোঝাতে সাহায্য করবে।

**৭. কাস্টমারঃ** আমি replacement চাই না। Screws আর brackets পাঠিয়ে দিলেই shelf ব্যবহার করতে পারবো।

**৮. এজেন্টঃ** আপনার preferred resolution হিসেবে missing hardware replacement note করছি স্যার। Seller-এর কাছে exact parts stock আছে কিনা আগে confirm করা হবে।

**৯. কাস্টমারঃ** Office setup আগামী সপ্তাহে শেষ করতে হবে। Seller response-এর জন্য অনেকদিন অপেক্ষা করা যাবে না।

**১০. এজেন্টঃ** আপনার business deadline ticket-এ উল্লেখ করছি স্যার। Parts dispatch সম্ভব হলে আলাদা shipment হিসেবে পাঠানো হবে, তবে seller confirmation ছাড়া date নিশ্চিত করতে চাই না।

**১১. কাস্টমারঃ** Local hardware shop থেকে screws কিনে নিলে কি warranty বা return নষ্ট হবে?

**১২. এজেন্টঃ** স্যার, নিজের মতো parts ব্যবহার করলে fit, stability বা warranty issue হতে পারে। Seller-এর specification না পাওয়া পর্যন্ত drilling বা assembly শুরু করবেন না।

**১৩. কাস্টমারঃ** Manual-ও নেই। Parts পেলে কি installation instruction online পাওয়া যাবে?

**১৪. এজেন্টঃ** স্যার, Seller manual বা assembly guide upload করতে পারে। আমি request-এ digital manual চেয়েছি, যাতে parts আসার পর নিজে assemble করতে পারেন।

**১৫. কাস্টমারঃ** Seller বলছে hardware packet আলাদা courier-এ পাঠাবে, কিন্তু কোনো tracking number দিচ্ছে না।

**১৬. এজেন্টঃ** Seller communication-এর screenshot রাখবেন স্যার। Official shipment create হলে tracking app-এ দেখা যাবে; tracking ছাড়া ব্যক্তিগত courier payment করবেন না।

**১৭. কাস্টমারঃ** যদি parts না পাঠায়, তাহলে কি পুরো furniture return করতে পারবো?

**১৮. এজেন্টঃ** জ্বী স্যার, Essential parts unavailable হলে product incomplete হিসেবে return বা refund review করা যায়। Panels ব্যবহার না করে original condition-এ রাখবেন।

**১৯. কাস্টমারঃ** Panels বড় এবং ভারী। Return pickup কি আমার office থেকে হবে?

**২০. এজেন্টঃ** আপনার address pickup coverage অনুযায়ী bulky-item pickup arrange করার request দিচ্ছি স্যার। Courier আগে call করে handling requirement জানাবে।

**২১. কাস্টমারঃ** Missing parts-এর complaint number এবং seller response-এর সময়টা বলবেন?

**২২. এজেন্টঃ** আপনার furniture parts reference DZ-FUR-২০২৬-০২৩। Seller-কে ৪৮ ঘণ্টার মধ্যে parts availability বা replacement resolution জানাতে বলা হয়েছে।

**২৩. কাস্টমারঃ** ঠিক আছে তানিম ভাই। আমি panels assemble না করে carton, damage আর missing hardware-এর ছবি upload করছি।

**২৪. এজেন্টঃ** ধন্যবাদ স্যার। Panels শুকনো জায়গায় রাখবেন, নিজে কাটাকাটি করবেন না এবং parts shipment এলে quantity মিলিয়ে তারপর assembly শুরু করবেন।

---

## সিনারিও ২৪ঃ Phone case নিজের mobile model-এ fit হচ্ছে না

> একজন student নিজের phone model-এর জন্য case অর্ডার করেছেন। Delivery-এর পর camera cutout, buttons এবং charging port align না হওয়ায় caseটি ব্যবহার করা যাচ্ছে না।

**১. কাস্টমারঃ** আপু, আমি আমার phone model দেখে case অর্ডার করেছিলাম, কিন্তু case লাগালে camera cutout আর buttons কোনোটাই ঠিকমতো align করছে না।

**২. এজেন্টঃ** Daraz customer care থেকে সাবরিনা বলছি স্যার। Compatibility issue-এর জন্য দুঃখিত। Product label-এ কোন model লেখা আছে?

**৩. কাস্টমারঃ** আমার phone Samsung A54, কিন্তু case-এর sticker-এ A54 5G লেখা। দেখতে একই হলেও camera opening আলাদা।

**৪. এজেন্টঃ** বুঝতে পারছি স্যার। Listing-এ model selection option এবং received case-এর label-এর ছবি মিলিয়ে দেখুন, কারণ regional variant-এ design পরিবর্তন হতে পারে।

**৫. কাস্টমারঃ** Listing-এ শুধু A54 লেখা ছিল, 5G বা variant আলাদা করে বলা ছিল না। তাই আমি সাধারণ A54 ধরে order করেছি।

**৬. এজেন্টঃ** স্যার, যদি listing information যথেষ্ট পরিষ্কার না হয়, এটি compatibility বা product description issue হিসেবে review করা যেতে পারে। Screenshot সংরক্ষণ করবেন।

**৭. কাস্টমারঃ** Caseটি একবার phone-এ লাগিয়েছিলাম। Camera block হওয়ায় সঙ্গে সঙ্গে খুলে ফেলেছি, কোনো scratch হয়নি।

**৮. এজেন্টঃ** ভালো করেছেন স্যার। Case ব্যবহার করবেন না এবং phone-এর সঙ্গে জোর করে fit করানোর চেষ্টা করবেন না। Product condition অক্ষত রাখবেন।

**৯. কাস্টমারঃ** আমি correct model-এর case চাই। Refund নিয়ে আবার order করলে delivery charge আবার দিতে হবে।

**১০. এজেন্টঃ** Replacement preference note করছি স্যার। Seller-এর কাছে exact compatible model থাকলে exchange review হবে; না থাকলে refund option দেওয়া হবে।

**১১. কাস্টমারঃ** Seller chat-এ বলছে, “A54 এবং A54 5G একই case,” কিন্তু বাস্তবে camera cutout একদম আলাদা।

**১২. এজেন্টঃ** Seller-এর message screenshot রাখবেন স্যার। Product fit না হওয়ার clear ছবি এবং phone model settings page-এর screenshotও upload করবেন।

**১৩. কাস্টমারঃ** Phone model settings-এর screenshot দিলে personal information leak হবে না তো?

**১৪. এজেন্টঃ** স্যার, IMEI বা ব্যক্তিগত data hide করে শুধু model name দেখানো screenshot upload করবেন। অপ্রয়োজনীয় security information কখনো শেয়ার করবেন না।

**১৫. কাস্টমারঃ** Return pickup না হওয়া পর্যন্ত case-এর packaging আর label কীভাবে রাখবো?

**১৬. এজেন্টঃ** Case, sticker, invoice এবং original pouch একসঙ্গে রাখবেন স্যার। Product-এ কাটাছেঁড়া বা additional sticker লাগাবেন না।

**১৭. কাস্টমারঃ** আমি student, তাই ছোট amount হলেও ভুল product-এর জন্য টাকা আটকে রাখা কষ্টকর।

**১৮. এজেন্টঃ** বুঝতে পারছি স্যার। Evidence দ্রুত upload করলে compatibility review শুরু হবে এবং eligible resolution অনুযায়ী refund বা replacement process এগোবে।

**১৯. কাস্টমারঃ** Correct case না পেলে কি আমি অন্য seller থেকে কিনে এই order refund নিতে পারবো?

**২০. এজেন্টঃ** স্যার, আপনি অন্য seller থেকে কিনতে পারেন, তবে এই order-এর return request আলাদাভাবে maintain করবেন। নতুন purchase-এর সঙ্গে পুরনো claim মিশবে না।

**২১. কাস্টমারঃ** Seller listing-এ model information ঠিক করবে তো? অন্যরা যেন একই ভুল না করে।

**২২. এজেন্টঃ** আপনার feedback listing quality team-এ পাঠাচ্ছি স্যার। Product variant পরিষ্কার না হলে seller-কে correction বা additional model details দেওয়ার নির্দেশনা যেতে পারে।

**২৩. কাস্টমারঃ** Support reference number দিন। আমি model screenshot আর case-এর ছবি upload করছি।

**২৪. এজেন্টঃ** আপনার compatibility reference DZ-MOB-২০২৬-০২৪। Phone model এবং case label দুটোই visible রাখবেন, তবে IMEI বা personal data ঢেকে upload করবেন।

**২৫. কাস্টমারঃ** ঠিক আছে সাবরিনা আপু। Case ব্যবহার না করে packagingসহ রেখে দিচ্ছি, ধন্যবাদ।

**২৬. এজেন্টঃ** আপনাকেও ধন্যবাদ স্যার। Return বা exchange update app-এ দেখবেন এবং pickup-এর সময় handover receipt সংগ্রহ করবেন।

---


