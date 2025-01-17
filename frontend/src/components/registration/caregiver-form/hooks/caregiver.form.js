export const generalInformations = [
  { id: "first_name", type: "text", name: "first_name", placeholder: "Unesite Vaše ime*" },
  { id: "last_name", type: "text", name: "last_name", placeholder: "Unesite Vaše prezime*" },
  { id: "email", type: "email", name: "email", placeholder: "Unesite Vaš E-mail*" },
  { id: "phone_number", type: "text", name: "phone_number", placeholder: "Unesite Vaš broj telefona*" },
  {
    id: "postal_code",
    type: "dropdown",
    name: "postal_code",
    placeholder: "Poštanski broj*",
    options: ["21000", "11000"],
  },
  { id: "city", type: "text", name: "city", placeholder: "Mesto stanovanja*" },
  { id: "birthdate", type: "text", name: "birthdate", placeholder: "Dan / Mesec / Godina rodjenja*" },
  {
    id: "gender",
    type: "dropdown",
    name: "gender",
    placeholder: "Pol*",
    options: ["muški", "ženski"],
  },
];

export const experienceAndQualifications = [
  {
    id: "work_application",
    type: "dropdown",
    name: "work_application",
    placeholder: "Prijava za rad*",
    options: ["prijava-rad"],
  },
  { id: "experience", type: "text", name: "experience", placeholder: "Iskustvo*" },
  {
    id: "weekly_days",
    type: "dropdown",
    name: "weekly_days",
    placeholder: "Dostupnost*",
    options: ["1", "2", "3", "4", "5", "6", "7"],
  },
  {
    id: "daily_hours",
    type: "text",
    name: "daily_hours",
    placeholder: "Koliko sati dnevno*",
  },
];
