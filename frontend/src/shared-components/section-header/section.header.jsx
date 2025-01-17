import React from "react";

import styles from "./section.header.module.scss";

import { Container } from "shared-components";

export const SectionHeader = ({ title, imageSrc }) => {
  return (
    <section className={styles.singleBlogTitle}>
      <Container styledClass={"singleBlogContainer"}>
        <h1 className={styles.h1}>{title}</h1>
        <div className={styles.singleBlogTitleImg}>
          <img className={styles.img} src={imageSrc} alt="" />
        </div>
      </Container>
    </section>
  );
};
