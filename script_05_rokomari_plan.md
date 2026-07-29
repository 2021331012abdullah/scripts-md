# Script 05: Rokomari.com — কাস্টমার সার্ভিস স্ক্রিপ্ট জেনারেশন প্ল্যান

**Script ID:** `ECOM_ROKOMARI`  
**Domain:** Book & Education Shopping E-commerce  
**Platform:** Rokomari.com  
**File:** `script_05_rokomari.md`  
**Total Scenarios:** 100  
**Call Types:** Inbound (70) + Outbound (30)

---

## Scenario Master List (100 Scenarios)

> **Legend:**  
> 📞 = Inbound (Customer calls)  
> 📤 = Outbound (Agent calls customer)

---

### A. Order & Delivery Issues (1-15)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 1 | 📞 | অর্ডার ট্র্যাকিং আপডেট না পাওয়া | Order tracking not updating for 5 days |
| 2 | 📞 | ভুল বই ডেলিভারি — অন্য কাস্টমারের বই পেয়েছে | Wrong book delivered — received another customer's order |
| 3 | 📞 | বই ছেঁড়া/ড্যামেজড অবস্থায় ডেলিভারি | Book delivered torn/damaged |
| 4 | 📞 | ডেলিভারি ম্যান ফোনে রিসিভ করছে না | Delivery rider not answering phone |
| 5 | 📞 | আংশিক ডেলিভারি — ৫টার মধ্যে ৩টা বই পেয়েছে | Partial delivery — got 3 out of 5 books |
| 6 | 📞 | ডেলিভারি অ্যাড্রেস পরিবর্তন করতে চান | Want to change delivery address after order |
| 7 | 📞 | একই বই দুইটা এসেছে, অন্য একটা বই অর্ডার ছিল | Duplicate book sent instead of different title |
| 8 | 📤 | ডেলিভারি শিডিউল কনফার্মেশন কল | Outbound call to confirm delivery schedule |
| 9 | 📞 | ঢাকার বাইরে ডেলিভারি কবে পাবে জানতে চান | Delivery timeline inquiry outside Dhaka |
| 10 | 📤 | ডেলিভারি ব্যর্থ — কাস্টমার বাসায় ছিলেন না | Failed delivery — customer was not home |
| 11 | 📞 | COD-তে ভাংতি নেই বলে ডেলিভারি দেয়নি | COD refused due to no change |
| 12 | 📞 | ডেলিভারি চার্জ বেশি দেখাচ্ছে | Delivery charge seems inflated |
| 13 | 📤 | লার্জ অর্ডার ভেরিফিকেশন কল | Large order verification call |
| 14 | 📞 | প্যাকেজিংয়ে পানি ঢুকে বই নষ্ট | Water damage during delivery |
| 15 | 📞 | ডেলিভারি ম্যান বিকাশে বেশি টাকা নিয়েছে | Delivery man overcharged via bKash |

---

### B. Product Quality & Condition (16-25)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 16 | 📞 | পুরাতন এডিশন এসেছে, নতুন এডিশন অর্ডার ছিল | Old edition sent instead of new |
| 17 | 📞 | বইয়ের মাঝখান থেকে ২০ পাতা মিসিং | 20 pages missing from middle |
| 18 | 📞 | ইংরেজি বই অর্ডার, বাংলা অনুবাদ এসেছে | Ordered English, got Bangla translation |
| 19 | 📞 | প্রিন্ট কোয়ালিটি খারাপ — ঝাপসা লেখা | Poor print quality — blurry text |
| 20 | 📞 | বইয়ের কভার ওয়েবসাইটের ছবির সাথে মিলছে না | Cover differs from website photo |
| 21 | 📞 | সেকেন্ড হ্যান্ড বই নতুন হিসেবে বিক্রি | Used book sold as new |
| 22 | 📞 | অরিজিনাল অর্ডার করেছি কিন্তু ফটোকপি এসেছে | Ordered original, received photocopy |
| 23 | 📞 | বাইন্ডিং খুলে গেছে, পাতা আলাদা হচ্ছে | Binding broken, pages falling apart |
| 24 | 📤 | ডেলিভারি পরবর্তী কোয়ালিটি ফিডব্যাক কল | Post-delivery quality feedback call |
| 25 | 📞 | ইম্পোর্টেড বইয়ে কাস্টমস ডিউটি কত জানতে চান | Imported book customs duty inquiry |

---

### C. Refund & Return (26-35)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 26 | 📞 | রিফান্ড ৭ দিন পরেও পাইনি | Refund not received after 7 days |
| 27 | 📞 | রিটার্ন পলিসি জানতে চান — বই খুলে পড়ে ফেলেছে | Return policy — book already read/opened |
| 28 | 📞 | ভুল বইয়ের জন্য রিটার্ন পিকআপ চান | Return pickup request for wrong book |
| 29 | 📤 | রিফান্ড প্রসেস কমপ্লিট — কাস্টমারকে জানানো | Outbound call confirming refund processed |
| 30 | 📞 | আংশিক রিফান্ড পেয়েছেন, পুরো টাকা চান | Partial refund received, wants full amount |
| 31 | 📞 | রিটার্ন রিকোয়েস্ট রিজেক্ট হয়েছে, কারণ জানতে চান | Return request rejected — wants reason |
| 32 | 📤 | রিটার্ন পিকআপ শিডিউলিং কল | Return pickup scheduling outbound call |
| 33 | 📞 | রিফান্ড বিকাশে চান, কার্ডে নয় | Wants refund to bKash instead of card |
| 34 | 📞 | গিফট হিসেবে পাওয়া বই রিটার্ন করতে চান | Returning a book received as gift |
| 35 | 📞 | ক্যানসেল করা অর্ডারের টাকা এখনো কাটা আছে | Money still deducted for cancelled order |

---

### D. Payment & Billing (36-45)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 36 | 📞 | অনলাইন পেমেন্ট ফেইল কিন্তু টাকা কাটা গেছে | Online payment failed but money deducted |
| 37 | 📞 | ডাবল চার্জ হয়ে গেছে একটা অর্ডারে | Double charged for single order |
| 38 | 📞 | বিকাশ পেমেন্ট ভেরিফাই হচ্ছে না | bKash payment not verifying |
| 39 | 📞 | ক্রেডিট কার্ড EMI অপশন কাজ করছে না | Credit card EMI option not working |
| 40 | 📤 | পেমেন্ট পেন্ডিং — রিমাইন্ডার কল | Payment pending reminder outbound call |
| 41 | 📞 | নগদ দিয়ে পেমেন্ট করতে চান, অপশন নেই | Wants to pay via Nagad, option unavailable |
| 42 | 📞 | ভাউচার/কুপন কোড কাজ করছে না | Voucher/coupon code not working |
| 43 | 📞 | স্টোর ক্রেডিট ব্যালেন্স দেখাচ্ছে না | Store credit balance not showing |
| 44 | 📤 | পেমেন্ট কনফার্মেশন ও ইনভয়েস কল | Payment confirmation and invoice outbound call |
| 45 | 📞 | প্রমোশনাল প্রাইস চার্জ হয়নি, ফুল প্রাইস কাটা | Promotional price not applied, full price charged |

---

### E. Pre-order & Stock (46-55)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 46 | 📞 | প্রি-অর্ডার করা বইয়ের ডেলিভারি ডেট জানতে চান | Pre-order delivery date inquiry |
| 47 | 📞 | আউট অফ স্টক বই কবে আসবে জানতে চান | When will out-of-stock book be available |
| 48 | 📤 | প্রি-অর্ডার বই এসেছে — কাস্টমারকে জানানো | Pre-order book arrived — notifying customer |
| 49 | 📞 | স্টক নোটিফিকেশন রিকোয়েস্ট সেটআপ | Request stock notification for specific book |
| 50 | 📤 | আউট অফ স্টক বই ব্যাক ইন স্টক নোটিফিকেশন | Back-in-stock notification outbound call |

---

### F. Gift & Special Services (51-58)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 51 | 📞 | গিফট র‍্যাপিং সার্ভিস কি আছে জানতে চান | Gift wrapping service inquiry |
| 52 | 📞 | গিফট মেসেজ কার্ড যোগ করতে চান অর্ডারে | Wants to add gift message card to order |
| 53 | 📞 | অন্য অ্যাড্রেসে গিফট হিসেবে পাঠাতে চান | Send as gift to different address |
| 54 | 📞 | গিফট ভাউচার কিনতে চান কাউকে দেওয়ার জন্য | Wants to buy gift voucher for someone |
| 55 | 📞 | গিফট ভাউচার রিডিম করতে পারছেন না | Cannot redeem gift voucher |
| 56 | 📞 | সারপ্রাইজ গিফট — ডেলিভারি ম্যান যেন আগে ফোন না করে | Surprise gift — delivery man should not call recipient first |
| 57 | 📞 | কর্পোরেট গিফটিং — ৫০টা বই একসাথে পাঠাতে চান | Corporate gifting — 50 books at once |
| 58 | 📤 | গিফট অর্ডার ডেলিভারি কনফার্মেশন কল | Gift order delivery confirmation outbound call |

---

### G. Bulk & Institutional Orders (59-65)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 59 | 📞 | স্কুল লাইব্রেরির জন্য ২০০ বই অর্ডার করতে চান | School library order — 200 books |
| 60 | 📞 | বাল্ক অর্ডারে ডিসকাউন্ট পাওয়া যাবে কিনা | Bulk order discount inquiry |
| 61 | 📤 | ইনস্টিটিউশনাল অর্ডার ফলো-আপ কল | Institutional order follow-up outbound call |
| 62 | 📞 | কোচিং সেন্টারের জন্য গাইড বই বাল্ক অর্ডার | Coaching center guide book bulk order |
| 63 | 📞 | NGO-র জন্য গ্রামে বই পাঠানোর ব্যবস্থা | NGO book distribution to rural areas |
| 64 | 📤 | বাল্ক অর্ডার ডেলিভারি শিডিউল কনফার্মেশন | Bulk order delivery schedule confirmation |
| 65 | 📞 | সরকারি প্রতিষ্ঠানের জন্য কোটেশন চান | Government institution quotation request |

---

### H. Account & Registration (66-72)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 66 | 📞 | একাউন্টে লগইন করতে পারছেন না — পাসওয়ার্ড ভুলে গেছেন | Cannot login — forgot password |
| 67 | 📞 | রেজিস্ট্রেশনে OTP আসছে না | OTP not received during registration |
| 68 | 📞 | ফোন নম্বর পরিবর্তন করতে চান একাউন্টে | Want to change phone number on account |
| 69 | 📞 | একাউন্ট ডিলিট করতে চান — ডেটা প্রাইভেসি | Want to delete account — data privacy concern |
| 70 | 📞 | অর্ডার হিস্ট্রি দেখা যাচ্ছে না | Order history not visible |
| 71 | 📞 | একই ইমেইলে দুইটা একাউন্ট হয়ে গেছে | Duplicate accounts with same email |
| 72 | 📤 | ইনঅ্যাক্টিভ কাস্টমার উইন-ব্যাক কল | Inactive customer win-back outbound call |

---

### I. Technical Support — App/Website (73-80)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 73 | 📞 | অ্যাপ ক্র্যাশ করছে বারবার | App crashing repeatedly |
| 74 | 📞 | ওয়েবসাইটে সার্চ কাজ করছে না | Website search not working |
| 75 | 📞 | কার্টে বই অ্যাড হচ্ছে না | Cannot add book to cart |
| 76 | 📞 | চেকআউট পেজে ঘুরে ঘুরে এরর দিচ্ছে | Checkout page giving error in loop |
| 77 | 📞 | অ্যাপ নোটিফিকেশন আসছে না | App notifications not working |
| 78 | 📞 | উইশলিস্ট সেভ হচ্ছে না, রিফ্রেশে মুছে যাচ্ছে | Wishlist not saving, clears on refresh |
| 79 | 📞 | রিভিউ লিখেছি কিন্তু পাবলিশ হচ্ছে না | Wrote review but not published |
| 80 | 📤 | অ্যাপ আপডেট করতে রিকোয়েস্ট কল | Outbound call requesting app update |

---

### J. Book Inquiry & Recommendations (81-88)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 81 | 📞 | HSC পরীক্ষার জন্য সেরা গাইড বই সাজেশন চান | Best HSC exam guide book suggestion |
| 82 | 📞 | ইসলামিক বইয়ের নতুন কালেকশন সম্পর্কে জানতে চান | Inquiry about new Islamic book collection |
| 83 | 📞 | বাচ্চাদের জন্য বয়স-উপযোগী বই সাজেশন | Age-appropriate children's book suggestion |
| 84 | 📞 | অথর-সাইনড কপি পাওয়া যাবে কিনা | Author-signed copy availability |
| 85 | 📞 | BCS প্রিপারেশনের জন্য কোন বই সেট কিনবে | Which book set for BCS preparation |
| 86 | 📞 | বইমেলার বই রকমারিতে কবে পাওয়া যাবে | When will book fair titles be on Rokomari |
| 87 | 📞 | ইংরেজি সেলফ-হেল্প বইয়ের বাংলা অনুবাদ আছে কিনা | Bangla translation of English self-help book |
| 88 | 📤 | পার্সোনালাইজড বুক রেকমেন্ডেশন কল | Personalized book recommendation outbound call |

---

### K. Offers, Promotions & Loyalty (89-93)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 89 | 📤 | বইমেলা সেল প্রমোশন কল | Book fair sale promotional outbound call |
| 90 | 📞 | ক্যাশব্যাক অফার পাইনি, শর্ত পূরণ হয়েছে | Cashback not received despite meeting conditions |
| 91 | 📤 | লয়্যালটি পয়েন্ট এক্সপায়ার হওয়ার আগে রিমাইন্ডার | Loyalty points expiry reminder outbound call |
| 92 | 📞 | ফ্রি ডেলিভারি অফার কাজ করছে না | Free delivery offer not applying |
| 93 | 📤 | বার্থডে স্পেশাল ডিসকাউন্ট অফার কল | Birthday special discount offer outbound call |

---

### L. Complaint & Escalation (94-97)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 94 | 📞 | তৃতীয়বার একই সমস্যা — সুপারভাইজারের সাথে কথা বলতে চান | Third time same issue — wants supervisor |
| 95 | 📞 | কাস্টমার কেয়ারে আগের কলে বিভ্রান্তিকর তথ্য দেওয়া হয়েছে | Misleading info given in previous call |
| 96 | 📞 | সোশ্যাল মিডিয়ায় কমপ্লেইন করবেন বলে হুমকি | Threatening to complain on social media |
| 97 | 📤 | আনরিসলভড কমপ্লেইন্ট ফলো-আপ কল | Unresolved complaint follow-up outbound call |

---

### M. Cancellation & Order Modification (98-100)

| # | Type | Bangla Title | English Reference |
|---|------|-------------|-------------------|
| 98 | 📞 | অর্ডার ক্যানসেল করতে চান — ভুল বই সিলেক্ট হয়েছে | Cancel order — wrong book selected |
| 99 | 📞 | অর্ডারে আরো বই যোগ করতে চান ডেলিভারির আগে | Add more books to existing order before delivery |
| 100 | 📞 | অর্ডার ক্যানসেল হয়ে গেছে নিজে থেকে — কারণ জানতে চান | Order auto-cancelled — wants to know reason |

---

## Execution Plan

### Chunking Strategy

| Parameter | Value |
|-----------|-------|
| Conversations per chunk | 4 |
| Total chunks | 25 |
| Chunk pattern | সিনারিও ১-৪, ৫-৮, ... ৯৭-১০০ |

### Category Distribution Across Chunks

| Chunk | Scenarios | Category |
|-------|-----------|----------|
| 1-4 | 1-15 | Order & Delivery |
| 5-7 | 16-25 | Product Quality |
| 7-9 | 26-35 | Refund & Return |
| 9-12 | 36-45 | Payment & Billing |
| 12-14 | 46-55 | Pre-order & Stock |
| 14-15 | 51-58 | Gift & Special |
| 15-17 | 59-65 | Bulk & Institutional |
| 17-18 | 66-72 | Account & Registration |
| 18-20 | 73-80 | Technical Support |
| 20-22 | 81-88 | Book Inquiry |
| 22-24 | 89-93 | Offers & Promotions |
| 24-25 | 94-100 | Complaint, Cancellation |

### Call Type Summary

| Type | Count | Percentage |
|------|-------|------------|
| 📞 Inbound | 72 | 72% |
| 📤 Outbound | 28 | 28% |
| **Total** | **100** | **100%** |

### Outbound Call Breakdown

| Category | Outbound Scenarios |
|----------|-------------------|
| Delivery confirmation/scheduling | 8, 10, 13, 58, 64 |
| Payment reminders | 40, 44 |
| Feedback & survey | 24, 88 |
| Stock notifications | 48, 50 |
| Follow-up & escalation | 29, 32, 61, 97 |
| Promotions & loyalty | 72, 80, 89, 91, 93 |

