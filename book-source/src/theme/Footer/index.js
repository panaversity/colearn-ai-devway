import React from 'react';
import {useThemeConfig} from '@docusaurus/theme-common';
import Link from '@docusaurus/Link';
import clsx from 'clsx';

function getSocialIcon(label) {
  switch (label.toLowerCase()) {
    case 'youtube':
      return <i className="fab fa-youtube footer-social-icon youtube" aria-hidden="true" />;
    case 'linkedin':
      return <i className="fab fa-linkedin footer-social-icon linkedin" aria-hidden="true" />;
    case 'instagram':
      return <i className="fab fa-instagram footer-social-icon instagram" aria-hidden="true" />;
    case 'facebook':
      return <i className="fab fa-facebook footer-social-icon facebook" aria-hidden="true" />;
    case 'github':
      return <i className="fab fa-github footer-social-icon github" aria-hidden="true" />;
    default:
      return null;
  }
}

function isSocialLink(label) {
  return [
    'youtube',
    'linkedin',
    'instagram',
    'facebook',
    'github',
  ].includes(label.toLowerCase());
}

export default function Footer() {
  const {footer} = useThemeConfig();
  if (!footer) {
    return null;
  }
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__links">
          {footer.links.map((linkCol, i) => (
            <div className="footer__col" key={i}>
              <div className="footer__title">{linkCol.title}</div>
              <ul className="footer__items">
                {linkCol.items.map((item, j) => (
                  <li key={item.href || item.to || j} className="footer__item">
                    <Link
                      className={clsx(
                        'footer__link-item',
                        isSocialLink(item.label) && 'footer__link-social',
                      )}
                      to={item.to}
                      href={item.href}
                      target={item.href ? '_blank' : undefined}
                      rel={item.href ? 'noopener noreferrer' : undefined}
                      aria-label={item.label}
                    >
                      {isSocialLink(item.label) && getSocialIcon(item.label)}
                      <span>{item.label}</span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        {footer.copyright && (
          <div className="footer__bottom">
            <div className="footer__copyright" dangerouslySetInnerHTML={{__html: footer.copyright}} />
          </div>
        )}
      </div>
    </footer>
  );
}