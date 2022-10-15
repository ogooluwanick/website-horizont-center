import React, { useRef } from "react";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass, faChevronDown, faAngleDown } from "@fortawesome/free-solid-svg-icons";
import styles from "./input.module.scss";

export const Input = ({ id, name, type, placeholder, hasError, options, required, valueChangeHandler }) => {
  if (type == "dropdown")
    return (
      <>
        <select
          onChange={(e) => valueChangeHandler(e.currentTarget.value)}
          name={name}
          id={id}
          className={styles.input + " " + styles.dropdown + " " + (hasError ? styles.hasError : null)}
        >
          {placeholder != null ? <option value="">{placeholder}</option> : null}
          {options.map((option) => {
            return <option value={option}>{option}</option>;
          })}
        </select>
        <FontAwesomeIcon icon={faChevronDown} className={styles.icon} />
      </>
    );
  else if (type == "search") {
    return (
      <>
        <input
          type={type}
          name={name}
          id={id}
          onChange={(e) => valueChangeHandler(e.currentTarget.value)}
          placeholder={placeholder}
          className={styles.input + " " + (hasError ? styles.hasError : null)}
        />
        <FontAwesomeIcon icon={faMagnifyingGlass} className={styles.icon} />
      </>
    );
  } else {
    return (
      <input
        type={type}
        name={name}
        id={id}
        onChange={(e) => valueChangeHandler(e.currentTarget.value)}
        placeholder={placeholder}
        className={styles.input + " " + (hasError ? styles.hasError : null)}
      />
    );
  }
};
